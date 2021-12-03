package mx.tec.lab;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.net.URL;
import java.util.concurrent.TimeUnit;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.springframework.boot.test.context.SpringBootTest;

import com.gargoylesoftware.htmlunit.WebClient;
import com.gargoylesoftware.htmlunit.html.HtmlButton;
import com.gargoylesoftware.htmlunit.html.HtmlListItem;
import com.gargoylesoftware.htmlunit.html.HtmlPage;
import com.gargoylesoftware.htmlunit.html.HtmlParagraph;
import com.gargoylesoftware.htmlunit.html.HtmlPasswordInput;
import com.gargoylesoftware.htmlunit.html.HtmlTextInput;

@SpringBootTest
class TouristPageTestApplicationTests {
	private static WebDriver driver;

    @BeforeEach
    public void setUp() {
        System.setProperty("webdriver.chrome.driver", "/Users/alejandroperez/Documents/MateriasTec/Software_quality_and_test/Selenium/chromedriver");
        driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
    }

    @AfterEach
    public void tearDown() {
        driver.quit();
    }
    

    @Test
    public void givenAClient_whenEnteringLoginCredentials_thenMainPageIsDisplayed() throws Exception {
        // When
        driver.get("https://tourist-guide-final-project.herokuapp.com/");
        WebElement emailField = driver.findElement(By.id("username"));
        emailField.sendKeys("tim@apple.com");
        WebElement passwordField = driver.findElement(By.id("password"));
        passwordField.sendKeys("SecretPwd1.");
        WebElement submitButton = driver.findElement(By.id("button-sign-in"));
        submitButton.click();   
        String testElement = driver.findElement(By.id("establishments-type")).getText();
        String title = driver.getTitle();
        String url = driver.getCurrentUrl();
        //System.out.println(url);
        //System.out.println(testElement);
        // Then
        assertEquals("museo", testElement);
        assertEquals("https://tourist-guide-final-project.herokuapp.com/establishments", url);
 
    }
    
	@Test
    public void givenAClient_isInMainPageAndClicksToAPlace_thenDetailsPageIsDisplayed() throws Exception {
        // When
        driver.get("https://tourist-guide-final-project.herokuapp.com/");
        WebElement emailField = driver.findElement(By.id("username"));
        emailField.sendKeys("tim@apple.com");
        WebElement passwordField = driver.findElement(By.id("password"));
        passwordField.sendKeys("SecretPwd1.");
        WebElement submitButton = driver.findElement(By.id("button-sign-in"));
        submitButton.click();   
        WebElement detailButton = driver.findElement(By.id("establishments-preview"));
        detailButton.click();
        
        
        String testElement = driver.findElement(By.id("container-establishment-info")).getText();
        String title = driver.getTitle();
        String url = driver.getCurrentUrl();
        //System.out.println(url);
        //System.out.println(testElement);
        // Then
        assertEquals(":", testElement);
        assertEquals("https://tourist-guide-final-project.herokuapp.com/establishment?id=61a6be1c9d65bdcea4a32833", url);
 
    }
	
	
	


}
