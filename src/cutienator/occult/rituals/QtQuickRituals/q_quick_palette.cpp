//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpalette_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25, mended on 2026-11-26: added by hand, rituals for
//  functions the generator leaves out: 1. Kept as it is when the generator
//  runs again.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpalette_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qpalette.h>
#include <cstring>

//  const QMetaObject *QQuickPalette::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QQuickPalette10metaObjectEv(
    const QQuickPalette *self) {
  return self->metaObject();
}

//  void *QQuickPalette::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QQuickPalette11qt_metacastEPKc(
    QQuickPalette *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPalette::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QQuickPalette11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPalette *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickPalette::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QQuickPalette2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPalette::tr(s, c, n));
}

//  QQuickPalette::QQuickPalette(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPalette *ritual_ZN13QQuickPaletteC1EP7QObject(QObject *parent) {
  return new QQuickPalette(parent);
}

//  QQuickColorGroup *QQuickPalette::active() const
extern "C" Q_DECL_EXPORT
QQuickColorGroup *ritual_ZNK13QQuickPalette6activeEv(
    const QQuickPalette *self) {
  return self->active();
}

//  QQuickColorGroup *QQuickPalette::inactive() const
extern "C" Q_DECL_EXPORT
QQuickColorGroup *ritual_ZNK13QQuickPalette8inactiveEv(
    const QQuickPalette *self) {
  return self->inactive();
}

//  QQuickColorGroup *QQuickPalette::disabled() const
extern "C" Q_DECL_EXPORT
QQuickColorGroup *ritual_ZNK13QQuickPalette8disabledEv(
    const QQuickPalette *self) {
  return self->disabled();
}

//  void QQuickPalette::resetActive()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPalette11resetActiveEv(QQuickPalette *self) {
  self->resetActive();
}

//  void QQuickPalette::resetInactive()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPalette13resetInactiveEv(QQuickPalette *self) {
  self->resetInactive();
}

//  void QQuickPalette::resetDisabled()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPalette13resetDisabledEv(QQuickPalette *self) {
  self->resetDisabled();
}

//  QPalette::ColorGroup QQuickPalette::currentColorGroup() const
extern "C" Q_DECL_EXPORT
QPalette::ColorGroup ritual_ZNK13QQuickPalette17currentColorGroupEv(
    const QQuickPalette *self) {
  return self->currentColorGroup();
}

//  void QQuickPalette::setCurrentGroup(QPalette::ColorGroup currentGroup)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPalette15setCurrentGroupEN8QPalette10ColorGroupE(
    QQuickPalette *self,
    QPalette::ColorGroup currentGroup) {
  self->setCurrentGroup(currentGroup);
}

//  void QQuickPalette::fromQPalette(QPalette palette)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPalette12fromQPaletteE8QPalette(
    QQuickPalette *self,
    const QPalette *palette) {
  self->fromQPalette(*palette);
}

//  QPalette QQuickPalette::toQPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK13QQuickPalette10toQPaletteEv(
    const QQuickPalette *self) {
  return new QPalette(self->toQPalette());
}

//  const QQuickAbstractPaletteProvider *QQuickPalette::paletteProvider()
//      const
extern "C" Q_DECL_EXPORT
const QQuickAbstractPaletteProvider *ritual_ZNK13QQuickPalette15paletteProviderEv(
    const QQuickPalette *self) {
  return self->paletteProvider();
}

//  void QQuickPalette::setPaletteProvider(const
//      QQuickAbstractPaletteProvider *paletteProvider)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPalette18setPaletteProviderEPK29QQuickAbstractPaletteProvider(
    QQuickPalette *self,
    const QQuickAbstractPaletteProvider *paletteProvider) {
  self->setPaletteProvider(paletteProvider);
}

//  void QQuickPalette::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPalette5resetEv(QQuickPalette *self) {
  self->reset();
}

//  void QQuickPalette::inheritPalette(const QPalette &palette)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPalette14inheritPaletteERK8QPalette(
    QQuickPalette *self,
    const QPalette *palette) {
  self->inheritPalette(*palette);
}

//  void QQuickPalette::setActive(QQuickColorGroup *active)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPalette9setActiveEP16QQuickColorGroup(
    QQuickPalette *self,
    QQuickColorGroup *active) {
  self->setActive(active);
}

//  void QQuickPalette::setInactive(QQuickColorGroup *inactive)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPalette11setInactiveEP16QQuickColorGroup(
    QQuickPalette *self,
    QQuickColorGroup *inactive) {
  self->setInactive(inactive);
}

//  void QQuickPalette::setDisabled(QQuickColorGroup *disabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPalette11setDisabledEP16QQuickColorGroup(
    QQuickPalette *self,
    QQuickColorGroup *disabled) {
  self->setDisabled(disabled);
}

//  void QQuickPalette::activeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPalette13activeChangedEv(QQuickPalette *self) {
  self->activeChanged();
}

//  void QQuickPalette::inactiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPalette15inactiveChangedEv(QQuickPalette *self) {
  self->inactiveChanged();
}

//  void QQuickPalette::disabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPalette15disabledChangedEv(QQuickPalette *self) {
  self->disabledChanged();
}

//  QQuickColorGroup::GroupPtr QQuickPalette::colorGroup(QPalette::ColorGroup
//      groupTag) const
extern "C" Q_DECL_EXPORT
QQuickColorGroup::GroupPtr *ritual_ZNK13QQuickPalette10colorGroupEN8QPalette10ColorGroupE(
    const QQuickPalette *self,
    QPalette::ColorGroup groupTag) {
  return new QQuickColorGroup::GroupPtr(self->colorGroup(groupTag));
}

//  QQuickColorGroup::GroupPtr
//      QQuickPalette::findColorGroup(QPalette::ColorGroup groupTag) const
extern "C" Q_DECL_EXPORT
QQuickColorGroup::GroupPtr *ritual_ZNK13QQuickPalette14findColorGroupEN8QPalette10ColorGroupE(
    const QQuickPalette *self,
    QPalette::ColorGroup groupTag) {
  return new QQuickColorGroup::GroupPtr(self->findColorGroup(groupTag));
}

//  void QQuickPalette::registerColorGroup(QQuickColorGroup *group,
//      QPalette::ColorGroup groupTag)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPalette18registerColorGroupEP16QQuickColorGroupN8QPalette10ColorGroupE(
    QQuickPalette *self,
    QQuickColorGroup *group,
    QPalette::ColorGroup groupTag) {
  self->registerColorGroup(group, groupTag);
}

//  bool QQuickPalette::isValidColorGroup(QPalette::ColorGroup groupTag,
//      const QQuickColorGroup::GroupPtr &colorGroup) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuickPalette17isValidColorGroupEN8QPalette10ColorGroupERK8QPointerI16QQuickColorGroupE(
    const QQuickPalette *self,
    QPalette::ColorGroup groupTag,
    const QQuickColorGroup::GroupPtr *colorGroup) {
  return self->isValidColorGroup(groupTag, *colorGroup);
}

//  QPalette::ColorGroup QQuickPalette::defaultCurrentGroup()
extern "C" Q_DECL_EXPORT
QPalette::ColorGroup ritual_ZN13QQuickPalette19defaultCurrentGroupEv() {
  return QQuickPalette::defaultCurrentGroup();
}

//  QPalette::ColorGroup QQuickPalette::currentColorGroup() const
extern "C" Q_DECL_EXPORT
QPalette::ColorGroup ritual_own_ZNK13QQuickPalette17currentColorGroupEv(
    const QQuickPalette *self) {
  return self->QQuickPalette::currentColorGroup();
}

//  a QQuickColorGroup::GroupPtr a ritual of QQuickPalette gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickPalette__QQuickColorGroup_GroupPtr(
    QQuickColorGroup::GroupPtr *self) {
  delete self;
}

//  void QQuickPalette::setColorGroup(QPalette::ColorGroup groupTag, const
//      QQuickColorGroup::GroupPtr &group, void (QQuickPalette::*)()
//      notifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPalette13setColorGroupEN8QPalette10ColorGroupERK8QPointerI16QQuickColorGroupEMS_FvvE(
    QQuickPalette *self,
    int groupTag,
    const QQuickColorGroup::GroupPtr *group,
    const char *notifier) {
  static const struct {
    const char *name;
    void (QQuickPalette::*member)();
  } known[] = {
      {"activeChanged", &QQuickPalette::activeChanged},
      {"inactiveChanged", &QQuickPalette::inactiveChanged},
      {"disabledChanged", &QQuickPalette::disabledChanged},
  };
  for (const auto &one : known) {
    if (!std::strcmp(one.name, notifier)) {
      self->setColorGroup(
          static_cast<QPalette::ColorGroup>(groupTag), *group,
          one.member);
      return;
    }
  }
  qFatal("no member function named %s here", notifier);
}
