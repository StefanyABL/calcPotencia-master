public static int calcPow (int base, int exp){
		if (exp==0){
			return 1;
		}
		
		return base* calcPow(base, exp-1);
	}