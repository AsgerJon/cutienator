//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qkeysequenceedit.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qkeysequenceedit.h>
#include <QtCore/qstring.h>
#include <QtGui/qkeysequence.h>

//  const QMetaObject *QKeySequenceEdit::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QKeySequenceEdit10metaObjectEv(
    const QKeySequenceEdit *self) {
  return self->metaObject();
}

//  QString QKeySequenceEdit::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QKeySequenceEdit2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QKeySequenceEdit::tr(s, c, n));
}

//  QKeySequenceEdit::QKeySequenceEdit(QWidget *parent)
extern "C" Q_DECL_EXPORT
QKeySequenceEdit *ritual_ZN16QKeySequenceEditC1EP7QWidget(QWidget *parent) {
  return new QKeySequenceEdit(parent);
}

//  QKeySequenceEdit::QKeySequenceEdit(const QKeySequence &keySequence,
//      QWidget *parent)
extern "C" Q_DECL_EXPORT
QKeySequenceEdit *ritual_ZN16QKeySequenceEditC1ERK12QKeySequenceP7QWidget(
    const QKeySequence *keySequence,
    QWidget *parent) {
  return new QKeySequenceEdit(*keySequence, parent);
}

//  QKeySequenceEdit::~QKeySequenceEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QKeySequenceEditD1Ev(QKeySequenceEdit *self) {
  delete self;
}

//  QKeySequence QKeySequenceEdit::keySequence() const
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZNK16QKeySequenceEdit11keySequenceEv(
    const QKeySequenceEdit *self) {
  return new QKeySequence(self->keySequence());
}

//  qsizetype QKeySequenceEdit::maximumSequenceLength() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK16QKeySequenceEdit21maximumSequenceLengthEv(
    const QKeySequenceEdit *self) {
  return self->maximumSequenceLength();
}

//  void QKeySequenceEdit::setClearButtonEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QKeySequenceEdit21setClearButtonEnabledEb(
    QKeySequenceEdit *self,
    bool enable) {
  self->setClearButtonEnabled(enable);
}

//  bool QKeySequenceEdit::isClearButtonEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QKeySequenceEdit20isClearButtonEnabledEv(
    const QKeySequenceEdit *self) {
  return self->isClearButtonEnabled();
}

//  void QKeySequenceEdit::setKeySequence(const QKeySequence &keySequence)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QKeySequenceEdit14setKeySequenceERK12QKeySequence(
    QKeySequenceEdit *self,
    const QKeySequence *keySequence) {
  self->setKeySequence(*keySequence);
}

//  void QKeySequenceEdit::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QKeySequenceEdit5clearEv(QKeySequenceEdit *self) {
  self->clear();
}

//  void QKeySequenceEdit::setMaximumSequenceLength(qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QKeySequenceEdit24setMaximumSequenceLengthEx(
    QKeySequenceEdit *self,
    qsizetype count) {
  self->setMaximumSequenceLength(count);
}
