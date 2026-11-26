//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qcoloroutput_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: added by hand, instances of templates of
//  the class: 1. Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qcoloroutput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>

//  QColorOutput::QColorOutput()
extern "C" Q_DECL_EXPORT
QColorOutput *ritual_ZN12QColorOutputC1Ev() {
  return new QColorOutput();
}

//  QColorOutput::~QColorOutput()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorOutputD1Ev(QColorOutput *self) {
  delete self;
}

//  bool QColorOutput::isSilent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QColorOutput8isSilentEv(const QColorOutput *self) {
  return self->isSilent();
}

//  void QColorOutput::setSilent(bool silent)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorOutput9setSilentEb(QColorOutput *self, bool silent) {
  self->setSilent(silent);
}

//  void QColorOutput::insertMapping(int colorID, ColorCode colorCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorOutput13insertMappingEi6QFlagsINS_18ColorCodeComponentEE(
    QColorOutput *self,
    int colorID,
    int colorCode) {
  self->insertMapping(
      colorID,
      QFlags<QColorOutput::ColorCodeComponent>::fromInt(colorCode));
}

//  void QColorOutput::writeUncolored(const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorOutput14writeUncoloredERK7QString(
    QColorOutput *self,
    const QString *message) {
  self->writeUncolored(*message);
}

//  void QColorOutput::write(const QStringView message, int color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorOutput5writeE11QStringViewi(
    QColorOutput *self,
    const QString *message,
    int color) {
  self->write(QStringView(*message), color);
}

//  void QColorOutput::writePrefixedMessage(const QString &message, QtMsgType
//      type, const QString &prefix)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorOutput20writePrefixedMessageERK7QString9QtMsgTypeS2_(
    QColorOutput *self,
    const QString *message,
    QtMsgType type,
    const QString *prefix) {
  self->writePrefixedMessage(*message, type, *prefix);
}

//  QString QColorOutput::colorify(QStringView message, int color) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QColorOutput8colorifyE11QStringViewi(
    const QColorOutput *self,
    const QString *message,
    int color) {
  return new QString(self->colorify(QStringView(*message), color));
}

//  void QColorOutput::flushBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorOutput11flushBufferEv(QColorOutput *self) {
  self->flushBuffer();
}

//  void QColorOutput::discardBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorOutput13discardBufferEv(QColorOutput *self) {
  self->discardBuffer();
}

//  void QColorOutput::write<void>(const QString &message, int color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorOutput5writeIvEEvRK7QStringi(
    QColorOutput *self,
    const QString *message,
    int color) {
  self->write<void>(*message, color);
}
