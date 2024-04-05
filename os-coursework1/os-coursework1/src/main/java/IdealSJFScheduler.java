import java.util.Comparator;
import java.util.Properties;
import java.util.PriorityQueue;

/**
 * Shortest Job First Scheduler
 *
 * @version 2017
 */
public class IdealSJFScheduler extends AbstractScheduler {
  //Implmentation based on Priority Queue based on process length
  //The lower the length of the next burst, the higher the priority
  private PriorityQueue<Process> readyQueue;
  public IdealSJFScheduler () {
    readyQueue = new PriorityQueue<Process>(Comparator.comparing(Process::getNextBurst));
  }
  /**
   * Adds a process to the ready queue.
   * usedFullTimeQuantum is true if process is being moved to ready
   * after having fully used its time quantum.
   */
  public void ready(Process process, boolean usedFullTimeQuantum) {
    readyQueue.offer(process);
  }

  /**
   * Removes the next process to be run from the ready queue
   * and returns it.
   * Returns null if there is no process to run.
   */
  public Process schedule() {

    System.out.println("Scheduler selects process "+readyQueue.peek());
    return readyQueue.poll();
  }
}
