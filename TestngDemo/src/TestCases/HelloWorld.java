package TestCases;

import org.testng.annotations.Test;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.AfterTest;
import org.w3c.dom.Document;
import org.openqa.selenium.By;
//添加对webdriver的引用
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver; 
import static org.junit.Assert.*;

//添加对DataProvider的引用
import CommonFunction.DataProvide;
import CommonFunction.DataReader;


public class HelloWorld extends DataProvide {
   public DataReader dr;//定义DataReader
	
  @Test(dataProvider = "Test_xml_dataprovider")//添加dataprovider
  public void f(Document params) throws Exception{
	  //System.out.println("Hello World!");
	  
	  WebDriver driver = new FirefoxDriver();//创建浏览器，并打开百度
	  
	  driver.get("http://www.bing.com");
	  
	  //查询从HellWorld.xml中读取的数据
	  Thread.sleep(5000);
	  WebElement input = driver.findElement(By.id("sb_form_q"));
	  input.click();
	  input.sendKeys(dr.readnodevalue(params, "hello", "name"));//读取Xml中的数据并输入到搜索框
	  Thread.sleep(2000);
	  WebElement submit = driver.findElement(By.id("sb_form_go"));	  
	  submit.click();	  
	  Thread.sleep(5000);
	  
	  //检测查询结果
	  WebElement result = driver.findElement(By.xpath(".//*[@id='b_results']/li[1]/div[1]/h2/a"));
	  String text = result.getText();
	  System.out.println(text);
	  assertNotEquals(0,text.indexOf(dr.readnodevalue(params, "hello", "name")));
	  driver.quit();
  }
  @BeforeTest
  public void beforeTest() throws Exception  {
	  //System.out.println("beforeTest running!");
	  dr=new DataReader();//实例化DataReader
	  init("src/TestData/HelloWorld.xml");//设置数据源
  }

  @AfterTest
  public void afterTest() {
	  System.out.println("afterTest running!");
  }

}
