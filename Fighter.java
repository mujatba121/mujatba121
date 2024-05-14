public class Fighter {
    // Member variables
    private String name;
    private int health;
    private int attackPower;
    
    // Constructor
    public Fighter(String name, int health, int attackPower) {
        this.name = name;
        this.health = health;
        this.attackPower = attackPower;
    }
    
    // Attack method
    public void attack(Fighter opponent) {
        opponent.reduceHealth(this.attackPower);
        System.out.println(this.name + " attacks " + opponent.getName() + " for " + this.attackPower + " damage!");
    }
    
    // Reduce opponent's health
    private void reduceHealth(int damage) {
        this.health -= damage;
    }
    
    // Check if fighter is alive
    public boolean isAlive() {
        return this.health > 0;
    }
    
    // Getter and Setter methods (if needed)
    public String getName() {
        return name;
    }
    
    public int getHealth() {
        return health;
    }
    
    public int getAttackPower() {
        return attackPower;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public void setHealth(int health) {
        this.health = health;
    }
    
    public void setAttackPower(int attackPower) {
        this.attackPower = attackPower;
    }
}
