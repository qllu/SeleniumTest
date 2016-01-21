package TestCases;
import org.w3c.dom.*;
import org.testng.annotations.Test;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.AfterTest; 
import CommonFunction.CommonFunctions;
import CommonFunction.DataProvide;
import CommonFunction.DataReader;
 
public class LoginTest extends DataProvide{
	
	public CommonFunctions comfun;
	public DataReader dr; 
	
	@BeforeTest
	public void setup() throws Exception{
	    String url = "https://qatest01.cybozu.cn";
	    comfun=new CommonFunctions(url);
	    dr=new DataReader();       
	    //设置数据源
	    init("src/TestData/LoginTest.xml");
	} 
	
	@Test(dataProvider="Test_xml_dataprovider")
	public void testlogin(Document params) throws Exception {   
		comfun.login(dr.readnodevalue(params, "login", "username"), dr.readnodevalue(params, "login", "password"));
		//comfun.checkequal(comfun.gettext("css", dr.readnodevalue(params, "login", "checkpoint1")), dr.readnodevalue(params, "login", "value1"));
		//退出登录
		comfun.logout();	 
	  }
	@AfterTest
	public void teardown() {
		comfun.teardown();
	}
}