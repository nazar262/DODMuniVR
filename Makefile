# ══════════════════════════════════════════════════════════════════════════════
#  DODM Homework Makefile
#  Usage examples:
#    make login   MAT=VR544201
#    make test
#    make submit-conio1
#    make submit-all
# ══════════════════════════════════════════════════════════════════════════════

SERVER   := wss://ta.di.univr.it/dodm
RTAL     := tools/bin/rtal
PYTHON   := python3 -u
VENV_ACT := source .venv/bin/activate &&

# Homework problems
PROBLEMS := conio1 triangolo piastrelle10 first_PD

# ── Paths ─────────────────────────────────────────────────────────────────────
sol   = solutions/$(1)/solution.py
exam  = homework/$(1)/$(1)/example.in.txt
expct = homework/$(1)/$(1)/example.out.txt

# ══════════════════════════════════════════════════════════════════════════════
# LOGIN  —  make login MAT=VR??????
# ══════════════════════════════════════════════════════════════════════════════
.PHONY: login
login:
ifndef MAT
	$(error Please provide your matriculation number: make login MAT=VR??????)
endif
	@echo "Logging in as $(MAT) to $(SERVER) ..."
	@$(RTAL) -s $(SERVER) login --username $(MAT)

# ══════════════════════════════════════════════════════════════════════════════
# STATUS / CHECK SUBMISSION RESULTS
# ══════════════════════════════════════════════════════════════════════════════

# Full scoreboard — shows all students' points + active multipliers
.PHONY: scoreboard
scoreboard:
	@$(RTAL) -s $(SERVER) connect scoreboard

# Check ONLY your own points row (pass your matriculation number)
#   make check-points MAT=VR544201
.PHONY: check-points
check-points:
ifndef MAT
	$(error Please provide: make check-points MAT=VR??????)
endif
	@echo "Fetching your points for $(MAT) ..."
	@$(RTAL) -s $(SERVER) connect scoreboard 2>&1 | grep -E "$(MAT)|Problem|Multiplier|Expiration|total"

# Download the scoreboard files (multipliers + points-to-marks map)
.PHONY: check-multipliers
check-multipliers:
	@$(RTAL) -s $(SERVER) get scoreboard -o /tmp/scoreboard_dodm.tar 2>&1
	@tar xf /tmp/scoreboard_dodm.tar -C /tmp/ 2>/dev/null || true
	@echo ""
	@echo "══ Active bonus multipliers ══"
	@cat /tmp/scoreboard/multipliers.yaml
	@echo ""
	@echo "══ Points → exam bonus marks ══"
	@cat /tmp/scoreboard/points2marks.yaml

# Check what services/subtasks are available for a problem
#   make check-problem PROB=conio1
.PHONY: check-problem
check-problem:
ifndef PROB
	$(error Please provide: make check-problem PROB=<problem_name>)
endif
	@echo "Services available for: $(PROB)"
	@$(RTAL) -s $(SERVER) list -v $(PROB)

# ══════════════════════════════════════════════════════════════════════════════
# LOCAL TESTS  —  make test
# ══════════════════════════════════════════════════════════════════════════════
.PHONY: test test-conio1 test-triangolo test-piastrelle10 test-first_PD

test: test-conio1 test-triangolo test-piastrelle10 test-first_PD

define TEST_RULE
test-$(1):
	@printf "Testing %-14s ... " "$(1)"
	@out=$$$$($(PYTHON) $(call sol,$(1)) < $(call exam,$(1)) 2>/dev/null); \
	 exp=$$$$(cat $(call expct,$(1))); \
	 if [ "$$$$out" = "$$$$exp" ]; then \
	   echo "✅  PASS"; \
	 else \
	   echo "❌  FAIL"; \
	   echo "  --- MY OUTPUT ---"; \
	   echo "$$$$out" | head -20; \
	   echo "  --- EXPECTED ---"; \
	   echo "$$$$exp" | head -20; \
	 fi
endef

$(foreach p,$(PROBLEMS),$(eval $(call TEST_RULE,$(p))))

# ══════════════════════════════════════════════════════════════════════════════
# SUBMIT (examples only — no score, just feedback)
#   make try-conio1
# ══════════════════════════════════════════════════════════════════════════════
.PHONY: try-conio1 try-triangolo try-piastrelle10 try-first_PD

try-%:
	@echo "── Dry-run (esempi_testo) for $* ──"
	$(RTAL) -s $(SERVER) connect $* solve -a size=esempi_testo \
	    -- $(PYTHON) $(call sol,$*)

# ══════════════════════════════════════════════════════════════════════════════
# SUBMIT FOR SCORE  (attaches source, counts toward homework)
#   make submit-conio1
#   make submit-all
# ══════════════════════════════════════════════════════════════════════════════
.PHONY: submit-conio1 submit-triangolo submit-piastrelle10 submit-first_PD submit-all

submit-%:
	@echo "── Submitting $* for score ──"
	$(RTAL) -s $(SERVER) connect \
	    -f source=$(call sol,$*) \
	    $* solve \
	    -- $(PYTHON) $(call sol,$*)

submit-all: submit-conio1 submit-triangolo submit-piastrelle10 submit-first_PD

# ══════════════════════════════════════════════════════════════════════════════
# SUBMIT SPECIFIC SIZE  (e.g. start with small before going big)
#   make submit-size PROB=conio1 SIZE=small
# ══════════════════════════════════════════════════════════════════════════════
.PHONY: submit-size
submit-size:
ifndef PROB
	$(error Usage: make submit-size PROB=<problem> SIZE=<size>)
endif
ifndef SIZE
	$(error Usage: make submit-size PROB=<problem> SIZE=<size>)
endif
	$(RTAL) -s $(SERVER) connect \
	    -f source=$(call sol,$(PROB)) \
	    $(PROB) solve -a size=$(SIZE) \
	    -- $(PYTHON) $(call sol,$(PROB))

# ══════════════════════════════════════════════════════════════════════════════
# HELP
# ══════════════════════════════════════════════════════════════════════════════
.PHONY: help
help:
	@echo ""
	@echo "  DODM Homework — available make targets:"
	@echo ""
	@echo "  ── Setup ────────────────────────────────────────────────────────────"
	@echo "  make login MAT=VR??????        Login to server with your matriculation number"
	@echo ""
	@echo "  ── Local testing ────────────────────────────────────────────────────"
	@echo "  make test                      Run all 4 solutions against local examples"
	@echo "  make test-conio1               Test one specific problem locally"
	@echo ""
	@echo "  ── Submission ───────────────────────────────────────────────────────"
	@echo "  make try-conio1                Dry-run on server (examples only, no score)"
	@echo "  make submit-conio1             Submit for score (all subtasks)"
	@echo "  make submit-all                Submit all 4 problems for score"
	@echo "  make submit-size PROB=conio1 SIZE=small   Submit up to a specific subtask"
	@echo ""
	@echo "  ── Check results after submission ───────────────────────────────────"
	@echo "  make scoreboard                Full scoreboard (all students + multipliers)"
	@echo "  make check-points MAT=VR?????? Your points row only"
	@echo "  make check-multipliers         Active bonus multipliers + points→marks table"
	@echo "  make check-problem PROB=conio1 Services and subtasks for a problem"
	@echo ""
	@echo "  Problems: $(PROBLEMS)"
	@echo ""
