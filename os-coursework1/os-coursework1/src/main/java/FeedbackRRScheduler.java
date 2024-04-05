import java.util.*;

/**
 * Feedback Round Robin Scheduler
 *
 * @version 2017
 */
public class FeedbackRRScheduler extends AbstractScheduler {
  private HashMap<Integer, Queue<Process>> multiLevelQueue;
  private Integer timeQuantum;
  /**
   * Adds a process to the ready queue.
   * usedFullTimeQuantum is true if process is being moved to ready
   * after having fully used its time quantum.
   */


  public FeedbackRRScheduler(){
    multiLevelQueue = new HashMap<>();
  }
  public void ready(Process process, boolean usedFullTimeQuantum) {
    int priority = process.getPriority();
    if (usedFullTimeQuantum) {
      // Increase the priority number (decrease priority level)
      priority++;
      process.setPriority(priority);
    }

    multiLevelQueue.putIfAbsent(priority, new LinkedList<>());
    multiLevelQueue.get(priority).add(process);

  }

  /**
   * Removes the next process to be run from the ready queue
   * and returns it.
   * Returns null if there is no process to run.
   */
  public Process schedule() {

    for (Integer priority : new TreeSet<>(multiLevelQueue.keySet())) {
      Queue<Process> queue = multiLevelQueue.get(priority);
      if (!queue.isEmpty()) {
        System.out.println("Scheduler selects process "+queue.peek());
        return queue.poll(); // Return and remove the process from the queue
      }
    }

    return null; // No process to run
  }

  public void initialise(Properties p){
    timeQuantum = Integer.parseInt(p.getProperty("timeQuantum"));
  }

  @Override
  public int getTimeQuantum(){
    return timeQuantum;
  }
  @Override
  public boolean isPreemptive(){
    return true;
  }
}
