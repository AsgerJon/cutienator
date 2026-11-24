//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicklistview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_listview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicklistview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickViewSection::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickViewSection10metaObjectEv(
    const QQuickViewSection *self) {
  return self->metaObject();
}

//  QString QQuickViewSection::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickViewSection2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickViewSection::tr(s, c, n));
}

//  QQuickViewSection::QQuickViewSection(QQuickListView *parent)
extern "C" Q_DECL_EXPORT
QQuickViewSection *ritual_ZN17QQuickViewSectionC1EP14QQuickListView(
    QQuickListView *parent) {
  return new QQuickViewSection(parent);
}

//  QString QQuickViewSection::property() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickViewSection8propertyEv(
    const QQuickViewSection *self) {
  return new QString(self->property());
}

//  void QQuickViewSection::setProperty(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickViewSection11setPropertyERK7QString(
    QQuickViewSection *self,
    const QString *a0) {
  self->setProperty(*a0);
}

//  SectionCriteria QQuickViewSection::criteria() const
extern "C" Q_DECL_EXPORT
QQuickViewSection::SectionCriteria ritual_ZNK17QQuickViewSection8criteriaEv(
    const QQuickViewSection *self) {
  return self->criteria();
}

//  void QQuickViewSection::setCriteria(SectionCriteria a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickViewSection11setCriteriaENS_15SectionCriteriaE(
    QQuickViewSection *self,
    QQuickViewSection::SectionCriteria a0) {
  self->setCriteria(a0);
}

//  QQmlComponent *QQuickViewSection::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK17QQuickViewSection8delegateEv(
    const QQuickViewSection *self) {
  return self->delegate();
}

//  void QQuickViewSection::setDelegate(QQmlComponent *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickViewSection11setDelegateEP13QQmlComponent(
    QQuickViewSection *self,
    QQmlComponent *delegate) {
  self->setDelegate(delegate);
}

//  QString QQuickViewSection::sectionString(const QString &value)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickViewSection13sectionStringERK7QString(
    QQuickViewSection *self,
    const QString *value) {
  return new QString(self->sectionString(*value));
}

//  int QQuickViewSection::labelPositioning() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickViewSection16labelPositioningEv(
    const QQuickViewSection *self) {
  return self->labelPositioning();
}

//  void QQuickViewSection::setLabelPositioning(int pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickViewSection19setLabelPositioningEi(
    QQuickViewSection *self,
    int pos) {
  self->setLabelPositioning(pos);
}

#endif  // QT_CONFIG(quick_listview)
