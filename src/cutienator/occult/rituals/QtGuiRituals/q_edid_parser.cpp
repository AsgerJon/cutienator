//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qedidparser_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if (QT_CONFIG(eglfs) || QT_CONFIG(xcb) || QT_CONFIG(direct2d) || defined(Q_OS_WIN))
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qedidparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  bool QEdidParser::parse(const QByteArray &blob)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QEdidParser5parseERK10QByteArray(
    QEdidParser *self,
    const QByteArray *blob) {
  return self->parse(*blob);
}

//  QEdidParser::~QEdidParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QEdidParserD1Ev(QEdidParser *self) {
  delete self;
}

#endif  // (QT_CONFIG(eglfs) || QT_CONFIG(xcb) || QT_CONFIG(direct2d) || defined(Q_OS_WIN))
