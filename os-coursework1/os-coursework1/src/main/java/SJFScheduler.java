import java.util.*;

/**
 * Shortest Job First Scheduler
 *
 * @version 2017
 */
public class SJFScheduler extends AbstractScheduler {

  //Implmentation based on Priority Queue based on process length
  private PriorityQueue<Process> readyQueue;
  private double initialBurstEstimate;
  private double alphaBurstEstimate;
  //<Id,nextBurst>
  private HashMap<Process,Double> priorityMap;
  public SJFScheduler(){
    priorityMap = new HashMap<>();
    readyQueue = new PriorityQueue<>(Comparator.comparingDouble(process -> priorityMap.getOrDefault(process, initialBurstEstimate)));
  }
  /**
   * Adds a process to the ready queue.
   * usedFullTimeQuantum is true if process is being moved to ready
   * after having fully used its time quantum.
   */
  public void ready(Process process, boolean usedFullTimeQuantum) {
    double estBurstValue;
    System.out.println("Enqueueing "+ process.getId()+" with est. burst ");
    if (process.getRecentBurst() == -1) {
      estBurstValue = initialBurstEstimate;
    } else {
      Double previousEstimate = priorityMap.getOrDefault(process, initialBurstEstimate);
      estBurstValue = alphaBurstEstimate * process.getRecentBurst() + (1 - alphaBurstEstimate) * previousEstimate;
    }

    priorityMap.put(process, estBurstValue);
    readyQueue.add(process);
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

  public void initialize(Properties p){
    initialBurstEstimate = Double.parseDouble(p.getProperty("initialBurstEstimate"));
    alphaBurstEstimate = Double.parseDouble(p.getProperty("alphaBurstEstimate"));
  }
}
