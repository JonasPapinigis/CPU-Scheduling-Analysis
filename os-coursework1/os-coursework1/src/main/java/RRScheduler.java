import java.util.*;

/**
 * Round Robin Scheduler
 *
 * @version 2017
 */
public class RRScheduler extends AbstractScheduler {

  int timeQuantum;
  Queue<Process> readyQueue;

  @Override
  public void initialize(Properties properties){
    timeQuantum = Integer.parseInt(properties.getProperty("timeQuantum"));
  }

  public RRScheduler(){
    readyQueue = new LinkedList<Process>();
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
  public int getTimeQuantum() {
    return timeQuantum;
  }

}
