# HabitPulse — Personal Habit & Fitness Accountability Coach

**Complete Project Document**

| | |
|---|---|
| **Project title** | HabitPulse: Personal Habit & Fitness Accountability Coach |
| **Author** | Anjali |
| **Domain** | Health & Wellness Technology / Applied AI |
| **Version** | 1.0 |
| **Date** | September 2026 |
| **License** | MIT |

---

## Table of Contents
1. Abstract
2. Preface
3. Introduction
4. Problem Statement
5. Objectives
6. Scope and Limitations
7. Literature Background
8. Requirements Specification
9. System Design
10. Coaching Logic
11. Implementation Plan
12. Core Code Sample
13. Testing Plan
14. Expected Results and Evaluation
15. Risks and Ethical Considerations
16. Roadmap and Future Scope
17. Conclusion
18. References
19. Appendix: Repository Structure and Setup

---

## 1. Abstract
HabitPulse is a lightweight, privacy-first web application that acts as a personal accountability coach. Users define habits and fitness goals, log their daily progress, and receive streak tracking, missed-habit follow-ups, weekly insights, and supportive coaching messages. The system combines a rule-based coaching engine with an optional AI layer. It is built with Python, FastAPI, SQLite, and Streamlit, and stores data locally by default. The project targets consistency, the main reason people abandon health goals, rather than simple data collection.

## 2. Preface
Starting a healthy habit is easy; sustaining it is hard. Most people drop new routines within weeks because nobody notices when they slip. A human coach or workout partner solves this through accountability, but such support is costly and not always available.

HabitPulse was conceived to close this gap with a personal, always-available coach that tracks habits and activity, notices patterns, and responds with timely, encouraging feedback.

**Guiding principles:** simplicity (logging in under 30 seconds), privacy (local-first data), positive reinforcement (never shaming), transparency (explainable coaching rules), and safety (general guidance only, with users directed to professionals for medical concerns).

**Intended audience:** individuals building daily routines, students and professionals seeking consistency, and developers interested in behaviour-tracking systems.

## 3. Introduction
Digital health tools have grown quickly, yet many focus on dashboards and numbers. Research on behaviour change highlights that self-monitoring, feedback, goal setting, and social accountability drive long-term adherence. HabitPulse brings these elements together in a single simple tool:

- **Self-monitoring:** habit, workout, and wellness logging
- **Goal setting:** SMART goals with deadlines
- **Feedback:** streaks, progress bars, weekly reports
- **Accountability:** daily check-ins and follow-ups on missed habits

## 4. Problem Statement
Existing habit and fitness apps commonly suffer from:
1. Generic reminders that users learn to ignore
2. Little response when a user misses days
3. Subscription costs, advertising, and data-privacy concerns
4. Complex interfaces that make daily logging tedious

There is a need for a simple, private, personalised tool that keeps users accountable and responds intelligently to their behaviour.

## 5. Objectives

### 5.1 Main Objective
To design and develop a personal habit and fitness accountability coach that helps users build and sustain healthy routines through consistent tracking, timely check-ins, and personalised feedback.

### 5.2 Specific Objectives
1. **Habit Management:** create, edit, archive, and track daily or weekly habits.
2. **Fitness Tracking:** record workouts, steps, water intake, sleep, and optional body metrics.
3. **Goal Setting:** support SMART goals with deadlines and visual progress.
4. **Accountability Engine:** generate daily check-ins and follow-ups when habits are missed.
5. **Motivation System:** implement streaks, milestones, and badges.
6. **Insights and Analytics:** provide weekly and monthly summaries and trend charts.
7. **Personalised Coaching:** deliver context-aware, supportive messages.
8. **Privacy and Portability:** store data locally and allow CSV export and deletion.
9. **Usability:** clean interface usable on desktop and mobile browsers.
10. **Maintainability:** modular, tested, well-documented code.

### 5.3 Success Criteria
| Metric | Target |
|---|---|
| Time to log a habit | < 30 seconds |
| Core feature test coverage | ≥ 80% |
| Page/API response time (local) | < 1 second |
| Streak calculation accuracy | 100% on test cases |
| Weekly report generation | < 3 seconds |
| Pilot user satisfaction (5–10 users) | ≥ 4 / 5 |

## 6. Scope and Limitations

**In scope (v1.0):** habit tracking, fitness logging, goals, streaks, check-ins, weekly insights, badges, CSV export, data deletion, rule-based coaching, optional AI coaching.

**Out of scope (v1.0):** medical diagnosis or treatment plans, wearable integration, social or competitive features, native mobile apps.

**Assumptions and constraints:** users log manually in v1.0; single-user local deployment first; optional AI features need an internet connection and an API key.

## 7. Literature Background
The design draws on established ideas in behavioural science and human-computer interaction:

- **Self-monitoring and feedback loops:** tracking behaviour increases awareness and adherence.
- **Goal-setting theory:** specific, measurable goals improve performance.
- **Habit formation research:** consistency and context cues matter more than intensity.
- **Streak mechanics and gamification:** visible streaks motivate continuation, though they must be designed so a single miss is not discouraging.
- **Implementation intentions ("if–then" plans):** planning when and where a habit occurs increases follow-through.

*(Add your specific citations in the References section before submission.)*

## 8. Requirements Specification

### 8.1 User Roles
- **User:** creates habits, logs progress, views insights.
- **Admin (future):** manages users and system settings.

### 8.2 Functional Requirements
| ID | Requirement | Priority |
|---|---|---|
| FR-01 | Create a user profile (name, goals, preferences) | High |
| FR-02 | Create, edit, archive habits with frequency | High |
| FR-03 | Mark a habit complete for a given day | High |
| FR-04 | Calculate current and longest streaks | High |
| FR-05 | Log workouts (type, duration, intensity, notes) | High |
| FR-06 | Log steps, water intake, sleep hours | Medium |
| FR-07 | Set goals with target value and date | High |
| FR-08 | Show goal progress visually | Medium |
| FR-09 | Issue daily check-in prompts | High |
| FR-10 | Detect missed habits and send follow-up | High |
| FR-11 | Generate weekly summary report | Medium |
| FR-12 | Award badges for milestones | Low |
| FR-13 | Generate personalised coaching messages | Medium |
| FR-14 | Export data to CSV | Medium |
| FR-15 | Delete all personal data | High |

### 8.3 Non-Functional Requirements
| ID | Category | Requirement |
|---|---|---|
| NFR-01 | Performance | Common actions respond in under 1 second |
| NFR-02 | Usability | Core actions within 3 clicks |
| NFR-03 | Security | Secrets via environment variables, never committed |
| NFR-04 | Privacy | Data stored locally by default |
| NFR-05 | Reliability | Data persisted after every write |
| NFR-06 | Portability | Runs on Windows, macOS, Linux |
| NFR-07 | Maintainability | Modular code, PEP 8, docstrings |
| NFR-08 | Accessibility | Readable contrast, keyboard navigable |

### 8.4 Use Cases
- **UC-1 Log habit completion:** user opens dashboard, selects habit, marks done, streak updates.
- **UC-2 Missed-habit follow-up:** no log by cutoff time, so the system sends an encouraging prompt.
- **UC-3 Weekly review:** user opens report and sees adherence, trends, and coach feedback.

## 9. System Design

### 9.1 Architecture
```
┌────────────┐     HTTP      ┌──────────────┐     ORM     ┌──────────┐
│ Streamlit  │ ────────────▶ │ FastAPI      │ ──────────▶ │ SQLite   │
│ UI         │ ◀──────────── │ Backend      │ ◀────────── │ Database │
└────────────┘               └──────┬───────┘             └──────────┘
                                    │
                          ┌─────────▼─────────┐
                          │ Coaching Engine   │
                          │ (rules + LLM opt.)│
                          └───────────────────┘
```

### 9.2 Modules
| Module | Responsibility |
|---|---|
| habits | CRUD for habits, completion logs |
| fitness | Workouts and health metrics |
| goals | Goal creation and progress |
| streaks | Streak calculation |
| checkins | Scheduling and missed-habit detection |
| insights | Weekly and monthly analytics |
| coach | Message generation |
| export | CSV export and data deletion |

### 9.3 Database Schema
```
User(id, name, created_at)
Habit(id, user_id, name, frequency, target, active)
HabitLog(id, habit_id, date, completed, note)
Workout(id, user_id, date, type, duration_min, intensity, notes)
Metric(id, user_id, date, steps, water_ml, sleep_hours, weight_kg)
Goal(id, user_id, title, target_value, current_value, due_date, status)
Badge(id, user_id, name, earned_at)
CheckIn(id, user_id, date, mood, message)
```

### 9.4 API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| POST | /habits | Create habit |
| GET | /habits | List habits |
| POST | /habits/{id}/log | Log completion |
| GET | /habits/{id}/streak | Get streak |
| POST | /workouts | Log workout |
| POST | /goals | Create goal |
| GET | /insights/weekly | Weekly report |
| GET | /export/csv | Export data |
| DELETE | /user/data | Delete all data |

### 9.5 Security and Privacy
Local-first storage, no third-party tracking, secrets in `.env`, and input validation on every endpoint.

## 10. Coaching Logic

**Rule-based layer (default):**
| Condition | Coach response |
|---|---|
| Streak reaches 7 days | Celebrate the milestone |
| Missed 1 day | Gentle reminder, no guilt |
| Missed 3 or more days | Suggest a smaller, easier version of the habit |
| Several high-intensity workouts in a row | Recommend a rest day |
| Goal reaches 50% / 100% | Progress celebration |

**Optional AI layer:** builds a short summary of recent logs and requests a supportive, non-medical coaching message from an LLM API. Keys come from environment variables and no personal identifiers are sent.

## 11. Implementation Plan

| Phase | Weeks | Deliverables |
|---|---|---|
| 1. Foundation | 1–2 | Repo setup, schema, habit CRUD, streak logic with tests |
| 2. Fitness and Goals | 3–4 | Workout and metric logging, goals, basic dashboard |
| 3. Accountability | 5–6 | Daily check-ins, missed-habit detection, rule-based coach |
| 4. Insights and Polish | 7–8 | Weekly reports, charts, badges, CSV export, pilot testing |

## 12. Core Code Sample

Streak calculation (`app/streaks.py`):

```python
from datetime import date, timedelta
from typing import Iterable, Tuple


def calculate_streaks(completed_dates: Iterable[date],
                      today: date | None = None) -> Tuple[int, int]:
    """Return (current_streak, longest_streak) for a set of completion dates."""
    today = today or date.today()
    days = sorted(set(completed_dates))
    if not days:
        return 0, 0

    # Longest streak
    longest = run = 1
    for prev, curr in zip(days, days[1:]):
        run = run + 1 if curr - prev == timedelta(days=1) else 1
        longest = max(longest, run)

    # Current streak: counts back from today (or yesterday if today not yet logged)
    day_set = set(days)
    cursor = today if today in day_set else today - timedelta(days=1)
    current = 0
    while cursor in day_set:
        current += 1
        cursor -= timedelta(days=1)

    return current, longest
```

Rule-based coach (`app/coach.py`):

```python
def coach_message(current_streak: int, days_missed: int) -> str:
    if days_missed >= 3:
        return ("It's been a few days, and that's okay. Let's restart small: "
                "try just 5 minutes today.")
    if days_missed >= 1:
        return "You missed a day. No problem. Get back on track today!"
    if current_streak and current_streak % 7 == 0:
        return f"{current_streak}-day streak! Fantastic consistency."
    return "Nice work today. Keep the momentum going."
```

Unit test (`tests/test_streaks.py`):

```python
from datetime import date, timedelta
from app.streaks import calculate_streaks


def test_seven_day_streak():
    today = date(2026, 9, 30)
    dates = [today - timedelta(days=i) for i in range(7)]
    assert calculate_streaks(dates, today) == (7, 7)


def test_streak_resets_after_gap():
    today = date(2026, 9, 30)
    dates = [today, today - timedelta(days=3), today - timedelta(days=4)]
    assert calculate_streaks(dates, today) == (1, 2)
```

## 13. Testing Plan

**Levels:** unit tests (streaks, goals, coach, dates), integration tests (API with test DB), manual UI walkthrough, and a user-acceptance pilot with 5–10 users.

| ID | Scenario | Expected result |
|---|---|---|
| TC-01 | Log habit 7 days in a row | Streak = 7 |
| TC-02 | Miss one day, then log | Current streak resets to 1; longest retained |
| TC-03 | Log same habit twice in a day | Counted once |
| TC-04 | Goal with past due date | Validation error |
| TC-05 | Missed 3 days | Coach suggests smaller habit |
| TC-06 | Export CSV | Correct headers and all logs |
| TC-07 | Delete user data | All records removed |
| TC-08 | Negative workout duration | Rejected with message |

**Tools:** pytest, pytest-cov, httpx.
**Exit criteria:** all high-priority tests pass, coverage ≥ 80%, no critical open bugs.

## 14. Expected Results and Evaluation
- Users can log a habit in under 30 seconds.
- Streaks and progress are calculated accurately.
- Users receive relevant follow-ups when they miss habits.
- Weekly reports clearly show adherence and trends.
- Pilot feedback is used to refine tone, timing, and features.

Evaluation will compare habit adherence rates across the pilot period and gather a short satisfaction survey (usability, motivation, usefulness of feedback).

## 15. Risks and Ethical Considerations
| Risk | Mitigation |
|---|---|
| Users treat the tool as medical advice | Clear disclaimer; general guidance only |
| Streak pressure causes discouragement | Supportive language; "restart small" messaging |
| Encouraging over-training or extreme dieting | Rest-day rules; no calorie-restriction advice |
| Privacy of health data | Local storage, export and delete features |
| AI messages being inappropriate | Constrained prompts; rule-based fallback |

## 16. Roadmap and Future Scope
- Optional LLM-powered coaching
- Email or Telegram reminders
- Wearable and health-app integration
- Multi-user support with authentication
- Mobile-friendly PWA
- Habit recommendations based on user history

## 17. Conclusion
HabitPulse addresses the central weakness of most wellness apps: the lack of meaningful accountability. By combining simple logging, streaks, goal tracking, and personalised, supportive feedback in a privacy-first design, it aims to help users move from short-lived motivation to lasting consistency. The modular architecture, documented requirements, and test plan make the project suitable for both real use and further extension.

## 18. References
*(Replace or extend with the sources you actually use.)*
1. Fogg, B.J. *Tiny Habits: The Small Changes That Change Everything.* 2019.
2. Clear, J. *Atomic Habits.* 2018.
3. Locke, E. & Latham, G. "Building a Practically Useful Theory of Goal Setting and Task Motivation." *American Psychologist*, 2002.
4. Lally, P. et al. "How Are Habits Formed: Modelling Habit Formation in the Real World." *European Journal of Social Psychology*, 2010.
5. FastAPI documentation: https://fastapi.tiangolo.com
6. Streamlit documentation: https://docs.streamlit.io
7. SQLAlchemy documentation: https://docs.sqlalchemy.org

## 19. Appendix: Repository Structure and Setup

```
habitpulse/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── requirements.txt
├── .gitignore
├── docs/
├── app/       # backend + coaching logic
├── ui/        # Streamlit interface
└── tests/     # unit tests
```

```bash
git clone https://github.com/<your-username>/habitpulse.git
cd habitpulse
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
streamlit run ui/app.py
```

---
*© 2026 Anjali. Released under the MIT License.*
