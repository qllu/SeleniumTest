package TestCases;

import org.testng.annotations.Test;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.AfterTest;
import org.w3c.dom.Document;
import org.openqa.selenium.By;
//��Ӷ�webdriver������
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver; 
import static org.junit.Assert.*;

//��Ӷ�DataProvider������
import CommonFunction.DataProvide;
import CommonFunction.DataReader;


public class HelloWorld extends DataProvide {
   public DataReader dr;//����DataReader
	
  @Test(dataProvider = "Test_xml_dataprovider")//���dataprovider
  public void f(Document params) throws Exception{
	  //System.out.println("Hello World!");
	  
	  WebDriver driver = new FirefoxDriver();//��������������򿪰ٶ�
	  
	  driver.get("http://www.bing.com");
	  
	  //��ѯ��HellWorld.xml�ж�ȡ������
	  Thread.sleep(5000);
	  WebElement input = driver.findElement(By.id("sb_form_q"));
	  input.click();
	  input.sendKeys(dr.readnodevalue(params, "hello", "name"));//��ȡXml�е����ݲ����뵽������
	  Thread.sleep(2000);
	  WebElement submit = driver.findElement(By.id("sb_form_go"));	  
	  submit.click();	  
	  Thread.sleep(5000);
	  
	  //����ѯ���
	  WebElement result = driver.findElement(By.xpath(".//*[@id='b_results']/li[1]/div[1]/h2/a"));
	  String text = result.getText();
	  System.out.println(text);
	  assertNotEquals(0,text.indexOf(dr.readnodevalue(params, "hello", "name")));
	  driver.quit();
  }
  @BeforeTest
  public void beforeTest() throws Exception  {
	  //System.out.println("beforeTest running!");
	  dr=new DataReader();//ʵ����DataReader
	  init("src/TestData/HelloWorld.xml");//��������Դ
  }

  @AfterTest
  public void afterTest() {
	  System.out.println("afterTest running!");
  }

}
