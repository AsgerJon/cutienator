//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>

//  QStackTextEngine::QStackTextEngine(const QString &string, const QFont &f)
extern "C" Q_DECL_EXPORT
QStackTextEngine *ritual_ZN16QStackTextEngineC1ERK7QStringRK5QFont(
    const QString *string,
    const QFont *f) {
  return new QStackTextEngine(*string, *f);
}

//  QStackTextEngine::~QStackTextEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QStackTextEngineD1Ev(QStackTextEngine *self) {
  delete self;
}
