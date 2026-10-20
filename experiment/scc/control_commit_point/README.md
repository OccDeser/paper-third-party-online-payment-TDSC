# Control experiment: commit point of IA-O2

The six protocol models of Table I, under the three channel assumptions
(base, secure_ms_channel, secure_ps_channel), with the user's commit for
IA-O2 (`U_Commit('UAuthMS', ...)`) moved to the receipt of the payment
result, as in the SCC model.

- `models/<assumption>/*.spthy`: the 18 models.
- `results/<assumption>/result.json`: Tamarin 1.10.0 results.

`U_MS_Order_Injective_Agreement` (IA-O2) is falsified in all 18 models,
so moving the commit point does not by itself make IA-O2 hold.
