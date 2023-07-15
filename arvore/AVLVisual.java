

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class AVLVisual extends JFrame {

    private AVLTree<Integer> avlTree;
    private AVLPanel avlPanel;

    public AVLVisual() {
        avlTree = new AVLTree<>();
        avlPanel = new AVLPanel();

        JButton insertButton = new JButton("Insert");
        insertButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String valueString = JOptionPane.showInputDialog("Insert a value:");
                try {
                    int value = Integer.parseInt(valueString);
                    avlTree.insert(value);
                    avlPanel.repaint();
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(null, "Invalid input! Please enter a valid integer value.",
                            "Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        });

        JButton deleteButton = new JButton("Delete");
        deleteButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String valueString = JOptionPane.showInputDialog("Delete a value:");
                try {
                    int value = Integer.parseInt(valueString);
                    avlTree.delete(value);
                    avlPanel.repaint();
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(null, "Invalid input! Please enter a valid integer value.",
                            "Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        });

        JPanel buttonPanel = new JPanel();
        buttonPanel.add(insertButton);
        buttonPanel.add(deleteButton);

        Container container = getContentPane();
        container.setLayout(new BorderLayout());
        container.add(avlPanel, BorderLayout.CENTER);
        container.add(buttonPanel, BorderLayout.SOUTH);

        setTitle("AVL Tree Visualization");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setVisible(true);
    }

    private class AVLPanel extends JPanel {

        private static final int CIRCLE_RADIUS = 20;
        private static final int LEVEL_HEIGHT = 80;

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            drawTree(g, getWidth() / 2, 50, getWidth() / 4, avlTree.getRoot());
        }

        private void drawTree(Graphics g, int x, int y, int hGap, AVLNode<Integer> node) {
            if (node != null) {
                g.drawOval(x - CIRCLE_RADIUS, y - CIRCLE_RADIUS, 2 * CIRCLE_RADIUS, 2 * CIRCLE_RADIUS);
                g.drawString(node.getValue().toString(), x - 4, y + 4);

                if (node.getLeft() != null) {
                    g.drawLine(x, y, x - hGap, y + LEVEL_HEIGHT);
                    drawTree(g, x - hGap, y + LEVEL_HEIGHT, hGap / 2, node.getLeft());
                }

                if (node.getRight() != null) {
                    g.drawLine(x, y, x + hGap, y + LEVEL_HEIGHT);
                    drawTree(g, x + hGap, y + LEVEL_HEIGHT, hGap / 2, node.getRight());
                }
            }
        }

        @Override
        public Dimension getPreferredSize() {
            return new Dimension(800, 600);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new AVLVisual();
            }
        });
    }
}
