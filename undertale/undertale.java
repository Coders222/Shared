import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.*;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.UnsupportedAudioFileException;




public class undertale extends JPanel implements KeyListener, MouseListener, Runnable{
	
	public static int gameState = 0;
	public static int mouseX;
	public static int mouseY;
	BufferedImage titleScreen;
	
	public undertale() {
		setPreferredSize(new Dimension(800, 500));
		setBackground(new Color(255, 255, 255));
		
		// import images
		try {
			titleScreen = ImageIO.read(new File("undertalestartmenu.png"));
			
		}
		catch (Exception e) {
			System.out.println("Image does not exist");
		}
		
		// create thread
		Thread thread = new Thread(this);
		thread.start();
		
		// add listeners
		addKeyListener(this);
		this.setFocusable(true);
		addMouseListener(this);
		
		// other
			

	}
	
	public static void main(String[] args) {
		JFrame frame = new JFrame("UNDERTALE");
		undertale panel = new undertale();
		frame.add(panel);
		frame.pack();
		frame.setVisible(true);
		frame.setResizable(false);

		
	}
	
	public void paintComponent(Graphics g) {
		
		// the start menu
		if (gameState == 0) {
			g.drawImage(titleScreen, 0, 0, null);
			
		}
			
	}

	@Override
	public void run() {
		System.out.println("yo");
		
	}

	
	@Override
	public void mousePressed(MouseEvent e) {
		// TODO Auto-generated method stub
		mouseX = e.getX();
		mouseY = e.getY();
		if (gameState == 0) {
			
			// play game
			if (295 <= mouseX && mouseX <= 535 && 150 <= mouseY && mouseY <= 215) {
				System.out.println("play");
			}
			
			// about 
			else if (295 <= mouseX && mouseX <= 535 && 243 <= mouseY && mouseY <= 310) {
				System.out.println("about");


			}
			
			else if (295 <= mouseX && mouseX <= 535 && 335 <= mouseY && mouseY <= 405) {
				System.out.println("quit");
				System.exit(0); // terminates the program
			}
			
			
			
		}
		
		
	}


	@Override
	public void keyPressed(KeyEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void keyReleased(KeyEvent e) {
		// TODO Auto-generated method stub
		
	}
	
	
	
	
	
	
///////////////////////////////////////////////////////	
	
	
	
	// useless methods
	
	@Override
	public void mouseClicked(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseEntered(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseExited(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void keyTyped(KeyEvent e) {
		// TODO Auto-generated method stub
		
	}

}
