//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qkeysequence_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(shortcut)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qkeysequence_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QKeySequencePrivate::QKeySequencePrivate()
extern "C" Q_DECL_EXPORT
QKeySequencePrivate *ritual_ZN19QKeySequencePrivateC1Ev() {
  return new QKeySequencePrivate();
}

//  QKeySequencePrivate::QKeySequencePrivate(const QKeySequencePrivate &copy)
extern "C" Q_DECL_EXPORT
QKeySequencePrivate *ritual_ZN19QKeySequencePrivateC1ERKS_(
    const QKeySequencePrivate *copy) {
  return new QKeySequencePrivate(*copy);
}

//  QString QKeySequencePrivate::keyName(Qt::Key key,
//      QKeySequence::SequenceFormat format)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QKeySequencePrivate7keyNameEN2Qt3KeyEN12QKeySequence14SequenceFormatE(
    Qt::Key key,
    QKeySequence::SequenceFormat format) {
  return new QString(QKeySequencePrivate::keyName(key, format));
}

//  QKeySequencePrivate::~QKeySequencePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QKeySequencePrivateD1Ev(QKeySequencePrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(shortcut)
