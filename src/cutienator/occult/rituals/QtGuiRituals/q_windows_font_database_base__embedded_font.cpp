//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qwindowsfontdatabasebase_p.h, Qt 6.12.0, as
//  the Qt of Windows installs it. Kept as it is when the generator
//  runs again.
//  Qt's library offers none of its functions by name, a class inside an
//  exported one being no exported class itself: only what its header
//  writes out is called.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qwindowsfontdatabasebase_p.h>
#include <QtCore/qbytearray.h>

//  QWindowsFontDatabaseBase::EmbeddedFont::EmbeddedFont(const QByteArray
//      &fontData)
extern "C" Q_DECL_EXPORT
QWindowsFontDatabaseBase::EmbeddedFont *ritual_ZN24QWindowsFontDatabaseBase12EmbeddedFontC1ERK10QByteArray(
    const QByteArray *fontData) {
  return new QWindowsFontDatabaseBase::EmbeddedFont(*fontData);
}

//  QByteArray QWindowsFontDatabaseBase::EmbeddedFont::data() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK24QWindowsFontDatabaseBase12EmbeddedFont4dataEv(
    const QWindowsFontDatabaseBase::EmbeddedFont *self) {
  return new QByteArray(self->data());
}

//  QWindowsFontDatabaseBase::EmbeddedFont::~EmbeddedFont()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWindowsFontDatabaseBase12EmbeddedFontD1Ev(
    QWindowsFontDatabaseBase::EmbeddedFont *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN)
