//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qbuttongroup.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qbuttongroup.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QButtonGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QButtonGroup10metaObjectEv(
    const QButtonGroup *self) {
  return self->metaObject();
}

//  QString QButtonGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QButtonGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QButtonGroup::tr(s, c, n));
}

//  QButtonGroup::QButtonGroup(QObject *parent)
extern "C" Q_DECL_EXPORT
QButtonGroup *ritual_ZN12QButtonGroupC1EP7QObject(QObject *parent) {
  return new QButtonGroup(parent);
}

//  QButtonGroup::~QButtonGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QButtonGroupD1Ev(QButtonGroup *self) {
  delete self;
}

//  void QButtonGroup::setExclusive(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QButtonGroup12setExclusiveEb(QButtonGroup *self, bool a0) {
  self->setExclusive(a0);
}

//  bool QButtonGroup::exclusive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QButtonGroup9exclusiveEv(const QButtonGroup *self) {
  return self->exclusive();
}

//  void QButtonGroup::addButton(QAbstractButton *a0, int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QButtonGroup9addButtonEP15QAbstractButtoni(
    QButtonGroup *self,
    QAbstractButton *a0,
    int id) {
  self->addButton(a0, id);
}

//  void QButtonGroup::removeButton(QAbstractButton *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QButtonGroup12removeButtonEP15QAbstractButton(
    QButtonGroup *self,
    QAbstractButton *a0) {
  self->removeButton(a0);
}

//  QAbstractButton *QButtonGroup::checkedButton() const
extern "C" Q_DECL_EXPORT
QAbstractButton *ritual_ZNK12QButtonGroup13checkedButtonEv(
    const QButtonGroup *self) {
  return self->checkedButton();
}

//  QAbstractButton *QButtonGroup::button(int id) const
extern "C" Q_DECL_EXPORT
QAbstractButton *ritual_ZNK12QButtonGroup6buttonEi(
    const QButtonGroup *self,
    int id) {
  return self->button(id);
}

//  void QButtonGroup::setId(QAbstractButton *button, int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QButtonGroup5setIdEP15QAbstractButtoni(
    QButtonGroup *self,
    QAbstractButton *button,
    int id) {
  self->setId(button, id);
}

//  int QButtonGroup::id(QAbstractButton *button) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QButtonGroup2idEP15QAbstractButton(
    const QButtonGroup *self,
    QAbstractButton *button) {
  return self->id(button);
}

//  int QButtonGroup::checkedId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QButtonGroup9checkedIdEv(const QButtonGroup *self) {
  return self->checkedId();
}
