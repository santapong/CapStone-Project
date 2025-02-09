import React from 'react'
import { PrismaClient } from '@prisma/client'

export default class DBQuery {
    constructor() {
        this.prisma = new PrismaClient();
    }

    async read(tableName, filter={}) {
        try {
            const data = await this.prisma[tableName].findMany({
                where : filter,
            });
            return data;
        } catch (error) {
            console.log('Error reading data', error)
            throw error
        } finally {
            await this.disconnect()
        }
    }

    async disconnect() {
        this.prisma.$disconnect();
        console.log('Disconnection from the database.')
    }
}