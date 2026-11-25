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

//  bool QTimeZonePrivate::NamePrefixMatch::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QTimeZonePrivate15NamePrefixMatchcvbEv(
    const QTimeZonePrivate::NamePrefixMatch *self) {
  return self->operator bool();
}

//  QTimeZonePrivate::NamePrefixMatch::~NamePrefixMatch()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTimeZonePrivate15NamePrefixMatchD1Ev(
    QTimeZonePrivate::NamePrefixMatch *self) {
  delete self;
}

#endif  // QT_CONFIG(timezone)
