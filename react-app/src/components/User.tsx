import { DataTypes, Model, Sequelize } from 'sequelize';
import bcrypt from 'bcrypt';

class User extends Model {
  declare id: number;
  declare email: string;
  declare password: string;

  static async hashPassword(password: string): Promise<string> {
    const salt = await bcrypt.genSalt(10);
    return await bcrypt.hash(password, salt);
  }
}

User.init(
  {
    id: {
      type: DataTypes.INTEGER,
      primaryKey: true,
      autoIncrement: true,
    },
    email: {
      type: DataTypes.STRING,
      allowNull: false,
      unique: true,
    },
    password: {
      type: DataTypes.STRING,
      allowNull: false,
    },
  },
  {
    sequelize: new Sequelize(), // Pass your Sequelize instance here
    modelName: 'User',
  }
);

export default User;