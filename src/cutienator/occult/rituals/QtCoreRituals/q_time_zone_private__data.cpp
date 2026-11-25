//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qtimezoneprivate_p.h, Qt 6.12.0, as
//  the Qt of macOS and of Windows install it. Kept as it is when the
//  generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(timezone)
#include <QtCore/6.12.0/QtCore/private/qtimezoneprivate_p.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qlist.h>
#include <QtCore/qlocale.h>
#include <QtCore/qstring.h>
#include <QtCore/qtimezone.h>

//  QTimeZonePrivate::Data::Data()
extern "C" Q_DECL_EXPORT
QTimeZonePrivate::Data *ritual_ZN16QTimeZonePrivate4DataC1Ev() {
  return new QTimeZonePrivate::Data();
}

//  QTimeZonePrivate::Data::Data(const QString &name, qint64 when, int
//      offset, int standard)
extern "C" Q_DECL_EXPORT
QTimeZonePrivate::Data *ritual_ZN16QTimeZonePrivate4DataC1ERK7QStringxii(
    const QString *name,
    qint64 when,
    int offset,
    int standard) {
  return new QTimeZonePrivate::Data(*name, when, offset, standard);
}

//  QTimeZonePrivate::Data::~Data()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTimeZonePrivate4DataD1Ev(QTimeZonePrivate::Data *self) {
  delete self;
}

#endif  // QT_CONFIG(timezone)
