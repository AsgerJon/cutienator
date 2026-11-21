//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qjsonparseerror.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qjsonparseerror.h>
#include <QtCore/qstring.h>

//  QString QJsonParseError::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QJsonParseError11errorStringEv(
    const QJsonParseError *self) {
  return new QString(self->errorString());
}

//  QJsonParseError::~QJsonParseError()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QJsonParseErrorD1Ev(QJsonParseError *self) {
  delete self;
}
