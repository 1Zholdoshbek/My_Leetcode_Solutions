type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };

function argumentsLength(...args: JSONValue[]): number {
    return arguments.length;
};

/**
 * argumentsLength(1, 2, 3); // 3
 */