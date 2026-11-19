//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qactiongroup.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qactiongroup.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>

//  const QMetaObject *QActionGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QActionGroup10metaObjectEv(
    const QActionGroup *self) {
  return self->metaObject();
}

//  QString QActionGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QActionGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QActionGroup::tr(s, c, n));
}

//  QActionGroup::QActionGroup(QObject *parent)
extern "C" Q_DECL_EXPORT
QActionGroup *ritual_ZN12QActionGroupC1EP7QObject(QObject *parent) {
  return new QActionGroup(parent);
}

//  QActionGroup::~QActionGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QActionGroupD1Ev(QActionGroup *self) {
  delete self;
}

//  QAction *QActionGroup::addAction(QAction *a)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN12QActionGroup9addActionEP7QAction(
    QActionGroup *self,
    QAction *a) {
  return self->addAction(a);
}

//  QAction *QActionGroup::addAction(const QString &text)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN12QActionGroup9addActionERK7QString(
    QActionGroup *self,
    const QString *text) {
  return self->addAction(*text);
}

//  QAction *QActionGroup::addAction(const QIcon &icon, const QString &text)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN12QActionGroup9addActionERK5QIconRK7QString(
    QActionGroup *self,
    const QIcon *icon,
    const QString *text) {
  return self->addAction(*icon, *text);
}

//  void QActionGroup::removeAction(QAction *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QActionGroup12removeActionEP7QAction(
    QActionGroup *self,
    QAction *a) {
  self->removeAction(a);
}

//  QAction *QActionGroup::checkedAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK12QActionGroup13checkedActionEv(
    const QActionGroup *self) {
  return self->checkedAction();
}

//  bool QActionGroup::isExclusive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QActionGroup11isExclusiveEv(const QActionGroup *self) {
  return self->isExclusive();
}

//  bool QActionGroup::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QActionGroup9isEnabledEv(const QActionGroup *self) {
  return self->isEnabled();
}

//  bool QActionGroup::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QActionGroup9isVisibleEv(const QActionGroup *self) {
  return self->isVisible();
}

//  ExclusionPolicy QActionGroup::exclusionPolicy() const
extern "C" Q_DECL_EXPORT
QActionGroup::ExclusionPolicy ritual_ZNK12QActionGroup15exclusionPolicyEv(
    const QActionGroup *self) {
  return self->exclusionPolicy();
}

//  void QActionGroup::setEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QActionGroup10setEnabledEb(QActionGroup *self, bool a0) {
  self->setEnabled(a0);
}

//  void QActionGroup::setDisabled(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QActionGroup11setDisabledEb(QActionGroup *self, bool b) {
  self->setDisabled(b);
}

//  void QActionGroup::setVisible(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QActionGroup10setVisibleEb(QActionGroup *self, bool a0) {
  self->setVisible(a0);
}

//  void QActionGroup::setExclusive(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QActionGroup12setExclusiveEb(QActionGroup *self, bool a0) {
  self->setExclusive(a0);
}

//  void QActionGroup::setExclusionPolicy(ExclusionPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QActionGroup18setExclusionPolicyENS_15ExclusionPolicyE(
    QActionGroup *self,
    QActionGroup::ExclusionPolicy policy) {
  self->setExclusionPolicy(policy);
}
