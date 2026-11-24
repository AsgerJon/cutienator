//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qcanframeprocessor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qcanframeprocessor.h>

//  QCanFrameProcessor::ParseResult::~ParseResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanFrameProcessor11ParseResultD1Ev(
    QCanFrameProcessor::ParseResult *self) {
  delete self;
}
