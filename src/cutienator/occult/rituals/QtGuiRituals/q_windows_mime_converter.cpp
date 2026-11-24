//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qwindowsmimeconverter.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if defined(Q_OS_WIN)
#include <QtGui/QtGui>
#include <QtGui/qwindowsmimeconverter.h>
#include <QtCore/qstring.h>

//  QWindowsMimeConverter::~QWindowsMimeConverter()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWindowsMimeConverterD1Ev(QWindowsMimeConverter *self) {
  delete self;
}

//  int QWindowsMimeConverter::registerMimeType(const QString &mimeType)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QWindowsMimeConverter16registerMimeTypeERK7QString(
    const QString *mimeType) {
  return QWindowsMimeConverter::registerMimeType(*mimeType);
}

#endif  // defined(Q_OS_WIN)
