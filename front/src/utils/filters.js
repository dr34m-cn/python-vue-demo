import {
	parseTime
} from "@/utils/utils";

const timeStampFilter = (value) => {
	return value ? parseTime(value) : '--';
}

export default {
	timeStampFilter
}