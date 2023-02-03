import java.util.Scanner;

import com.adventofcode.hiraganime.model.Exercise;

/**
 * @DAY_1
 * 
 * @NOT_QUITE_LISP
 * 
 * @PROBLEM_STATEMENT
 * 
 * Any person is trying to deliver presents in a large apartment building, 
 * but he can't find the right floor - the directions he got are a little confusing. 
 * He starts on the ground floor (floor 0) and then follows the instructions one character at a time.
 * 
 * An opening parenthesis, (, means he should go up one floor, 
 * and a closing parenthesis, ), means he should go down one floor.
 * 
 * The apartment building is very tall, and the basement is very deep; 
 * he will never find the top or bottom floors.
 * 
 * @PROBLEM_EXAMPLE
 * 
 * - (()) and ()() both result in floor 0.
 * - ((( and (()(()( both result in floor 3.
 * - ))((((( also results in floor 3.
 * - ()) and ))( both result in floor -1 (the first basement level).
 * - ))) and )())()) both result in floor -3.
 * 
 *  To what floor do the instructions take this person?
 *  
 *  @SOLUTION_AUTHOR BrandonMartinez-jar
 *  @SOLUTION_LANGUAGE Java
 *  @SOLUTION_DATE 30/01/2023
 * 
 */

public class Day_1 implements Exercise{
	
	public Scanner console = new Scanner(System.in); // <- Console input configurations
	
	@Override
	public void execute() {
		
		Day_1 exercise = new Day_1();
		
		int response = exercise.algorithm(exercise.console.nextLine()); // <- Console input request

		System.out.println(response); // <- Console output response
	}
	
	/**
	 * 
	 * @method algorithm
	 * 
	 * This method split the input string storing each '(' or ')' 
	 * to a position in a array and make a count where:
	 * 
	 * - Each '(' is + 1 
	 * - Each ')' is - 1
	 * 
	 * @param String input, That contain the input of console
	 * 
	 * @return the result of the count requested in the original statement
	 * 
	 */
	
	public int algorithm(String input) {
		
		int count = 0;
		
		for(String c : input.split("")) {
			count = (c.equals("(")) ? count + 1 : count - 1;
		}
		
		return count;
	}

}
