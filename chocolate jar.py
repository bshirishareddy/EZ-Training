def sort_packets(packets):
    packets_with_chocolates = []
    empty_packets = []

    # First loop to separate packets with chocolates
    for packet in packets:
        if packet:
            packets_with_chocolates.append(packet)

    # Second loop to separate empty packets
    for packet in packets:
        if not packet:
            empty_packets.append(packet)

    # Combine the lists with packets with chocolates first, then empty packets
    return packets_with_chocolates + empty_packets

# Example usage:
packets = [[4], [], [5], [], [1], [9], [], []]
sorted_packets = sort_packets(packets)
print(sorted_packets)




