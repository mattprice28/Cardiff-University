package Objects;

import static com.jogamp.opengl.GL.GL_ARRAY_BUFFER;
import static com.jogamp.opengl.GL.GL_STATIC_DRAW;

import java.nio.FloatBuffer;

public class SCube extends SObject{
	private int numVertices = 36;
	private int vPosition;
	private int vColor;
		
	public SCube(){	
		super();
		update();
	}
		
	@Override
	protected void genData() {


		float [] vertexArray = { //define triangles in anti-clockwise direction 
				// front face
				 1,  1,  1,    // triangle 1
				-1,  1,  1,
				-1, -1,  1,
				 1,  1,  1,    // triangle 2
				-1, -1,  1,
				 1, -1,  1,
				// back face
				 1,  1, -1,    // triangle 1
				-1, -1, -1,
				-1,  1, -1,
				 1,  1, -1,    // triangle 2
				 1, -1, -1,
				-1, -1, -1,
				// left face
				-1,  1,  1,    // triangle 1
				-1,  1, -1,
				-1, -1,  1,
				-1,  1, -1,    // triangle 2
				-1, -1, -1,
				-1, -1,  1,
				// right face
				 1,  1,  1,    // triangle 1
				 1, -1,  1,
				 1,  1, -1,
				 1,  1, -1,    // triangle 2
				 1, -1,  1,
				 1, -1, -1,
				// top face
				 1,  1,  1,    // triangle 1
				 1,  1, -1,
				-1,  1,  1,
				-1,  1,  1,    // triangle 2
				 1,  1, -1,
				-1,  1, -1,
				// bottom face
				 1, -1,  1,    // triangle 1
				-1, -1,  1,
				 1, -1, -1,
				-1, -1,  1,    // triangle 2
				-1, -1, -1,
				 1, -1, -1
				
		};
		


		//same color on each side
		float [] colorArray = {
				1, 0, 0,  //Front color
				1, 0, 0,
				1, 0, 0,
				1, 0, 0,
				1, 0, 0,
				1, 0, 0,
				0, 1, 0,  //Back color
				0, 1, 0,
				0, 1, 0,
				0, 1, 0,
				0, 1, 0,
				0, 1, 0,
				0, 0, 1,  //Left color
				0, 0, 1,
				0, 0, 1,
				0, 0, 1,
				0, 0, 1,
				0, 0, 1,
				1, 1, 0,  //Right color
				1, 1, 0,
				1, 1, 0,
				1, 1, 0,
				1, 1, 0,
				1, 1, 0,
				1, 0, 1,  //Top color
				1, 0, 1,
				1, 0, 1,
				1, 0, 1,
				1, 0, 1,
				1, 0, 1,
				0, 1, 1,  //Bottom color
				0, 1, 1,
				0, 1, 1,
				0, 1, 1,
				0, 1, 1,
				0, 1, 1,
				
		};

		FloatBuffer vertices = FloatBuffer.wrap(vertexArray);
		FloatBuffer colors = FloatBuffer.wrap(colorArray);
				
	}
}