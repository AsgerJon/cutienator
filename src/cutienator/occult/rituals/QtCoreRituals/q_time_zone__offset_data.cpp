//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtimezone.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(timezone)
#include <QtCore/qtimezone.h>

//  QTimeZone::OffsetData::~OffsetData()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeZone10OffsetDataD1Ev(QTimeZone::OffsetData *self) {
  delete self;
}

#endif  // QT_CONFIG(timezone)
