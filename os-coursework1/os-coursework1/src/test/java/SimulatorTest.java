import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.util.Enumeration;
import java.util.Properties;
import java.io.File;

import static org.junit.jupiter.api.Assertions.*;

class SimulatorTest {
/**
    String[] args = {"src/test/java/simulator_parameters.prp","src/test/java/output.out","src/test/java/inputs.in"};
    Properties props = new Properties();
    File params = new File(args[0]);
    @BeforeEach
    void init(){
        Properties props = new Properties();
        File params = new File(args[0]);
        try {
            props.load(new FileInputStream(params));
        } catch (
        FileNotFoundException e) {
            System.exit(1);
        } catch (IOException e) {
            System.exit(1);
        }
        System.out.println(props);
    }

    @Test
    void testParametersCorrectlyLoaded(){

        assertEquals("20",props.getProperty("timeQuantum"));
    }
    @Test
    void testRRSchedulerLaunched(){
        RRScheduler scheduler = new RRScheduler();
        scheduler.initialize(props);
        assertAll("Multiple Assertions",
                () -> assertEquals(20,scheduler.getTimeQuantum()),
                () -> assertFalse(scheduler.isPreemptive()));

    }
    */
}