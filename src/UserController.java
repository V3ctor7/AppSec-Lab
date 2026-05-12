import java.sql.*;
import javax.servlet.http.*;

public class UserController {

    // Vulnerability 1: SQL Injection (CWE-89)
    public User getUser(HttpServletRequest request) throws SQLException {
        String userId = request.getParameter("id");
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/mydb");
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery("SELECT * FROM users WHERE id = '" + userId + "'");
        return mapUser(rs);
    }

    // Vulnerability 2: XSS - Reflected (CWE-79)
    public void search(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String query = request.getParameter("q");
        response.getWriter().println("<h1>Results for: " + query + "</h1>");
    }

    // Vulnerability 3: Hardcoded credentials (CWE-798)
    public Connection getAdminConnection() throws SQLException {
        String password = "SuperSecret123!";
        return DriverManager.getConnection("jdbc:mysql://localhost/mydb", "admin", password);
    }

    private User mapUser(ResultSet rs) { return null; }
}

class User {}
