public class PrepareTax{
    public static void main [String[] args] {
        int income = 5000; //gross income of the individual in dollars.
        double taxRate = .20; //tax rate as a decimal (i.e.,
        //a 20% tax rate is represented by .20)
        
        System.out.println("The amount of tax owed for an " +
                           "individual with a gross income of $" +
                            income + " and a tax rate of " +
                             taxRate + "% is: ");
        System.out.println(calculateTax(income, taxRate));
    }
    
    /* This method takes two parameters - income and taxRate - and returns the amount of tax that should be paid given these inputs. The formula used to calculate this
    /*This method takes two parameters: income and taxRate. It returns the amount of tax that should be paid based on these inputs. The formula used to calculate this is:
    /* This method takes two parameters: income and taxRate. It returns the amount of tax that should be paid based on these inputs. */
    /* This method calculates the amount of tax owed based on the given income and tax rate */
    public static double calculateTax(int income, double taxRate){
        return income * taxRate;
    }
}           
/*
Explanation:
This program first initializes two variables, income and taxRate. The income variable represents the total money earned by an individual before any deductions or taxes are taken into account. TaxRate represents
This program first initializes two variables, income and taxRate. Income represents the total money earned by an individual before any deductions or taxes are taken into account, while taxRate represents
}