Task for Nikhil: User should be able to input a question and it gets a series a frames that explain how to solve that question (diagrams/drawing steps with text/number as well when needed)

For example, if I ask 'how to find the hypotenuse length if one side 3 cm and another is 4 cm?' it should give me a video of a right triangle with each side labeled 3 and 4 and the formula for pythagorem thm a^2+b^2=c^2 plugging in values etc



---------------------------------------------------------------------------------------------------

Steps to run and test all of this code

Advice: (it's up to you but you can copy all of this into jupyter notebook or run on terminal, i prefer jupyter as its simple to see output)

1. Run all the functions/prompts
  a. render_diagram_with_latex_steps
  b. parse_openai_diagram_output
  c. steps_prompt
  d. drawing_prompt

2. Run the 1st openAI call (its labeled 'first api call' in a comment)
3. Run the 2nd openAI call (its labeled 'second api call' in a comment)




---------------------------------------------------------------------------------------------------


So how does this all work? ( I have added comments but explaining it here as well)

1. Call 1st open_ai function to generate steps that answer the question. If you ask gpt for drawing steps directly from a question, it gets a bit confused and doesn't draw clear steps so thats why we are asking for steps on how to solve the question first

2. Call 2nd open_ai function to take those steps and generate diagrams instructions and script from those steps
  
3. These steps would then be filtered/passed into "parse_openai_diagram_output" function
Note: "parse_openai_diagram_output" is a function that takes Open_AI english drawing steps and converts to mathplotlib formatted steps

6. Call render_diagram_with_latex_steps(drawing_steps, question = question, output_folder="frames")
Note: This would create the images for each mathplotlib drawn out step.

Note: I have not included the audio and video aspect code because lets not waste elevenlabs api key (this costs money each time you use so first work on the frames)

---------------------------------------------------------------------------------------------------