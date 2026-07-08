# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

User should be able to add basic info about themselves the pet owner

User should be able to add basic info about thier pet and optionally care notes

User should be able add or edit or delete pet care tasks like ike feeding, walking, medication, grooming

User should be able to ask the app to create a schedule that fits the available time and prioritizes the most important care tasks.

User should optionally be able to view explanation of the schedule


The Owner class stores basic information about the pet owner and keeps a list of all pets they care for. The owner can add pets, remove pets, view all pets, and find a specific pet.

The Pet class stores identifying information about a specific pet and manages that pet’s care tasks. Each pet has its own task list, such as feeding, walking, grooming, or medication tasks.

The Task class represents a single pet care responsibility. It includes what needs to be done, when it is due, how important it is, how long it should take, and whether it has been completed.

The Scheduler class works across multiple pets, not just one pet. It collects tasks from every pet owned by the user, filters out completed tasks, sorts tasks by urgency and priority, and generates a daily care plan based on the owner’s available time.
**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
Add missing rationale attribute to task, also added a priority class with Enum for easier sorting

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
