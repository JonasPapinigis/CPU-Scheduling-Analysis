import java.util.*;

/**
 * Feedback Round Robin Scheduler
 * 
 * @version 2017
 */
public class FeedbackRRScheduler extends AbstractScheduler {

  int timeQuantum;
  Queue<Process> readyQueue;

  @Override
  public void initialize(Properties parameters) {

  }

  public void ready(Process process, boolean usedFullTimeQuantum) {

    // TODO

  }

  /**
   * Removes the next process to be run from the ready queue 
   * and returns it. 
   * Returns null if there is no process to run.
   */
  public Process schedule() {

    // TODO

    return null;
  }
}
