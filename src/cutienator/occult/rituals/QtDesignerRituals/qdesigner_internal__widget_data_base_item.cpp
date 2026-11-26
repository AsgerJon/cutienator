//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/widgetdatabase_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/widgetdatabase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

//  qdesigner_internal::WidgetDataBaseItem::WidgetDataBaseItem(const QString
//      &name, const QString &group)
extern "C" Q_DECL_EXPORT
qdesigner_internal::WidgetDataBaseItem *ritual_ZN18qdesigner_internal18WidgetDataBaseItemC1ERK7QStringS3_(
    const QString *name,
    const QString *group) {
  return new qdesigner_internal::WidgetDataBaseItem(*name, *group);
}

//  QString qdesigner_internal::WidgetDataBaseItem::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal18WidgetDataBaseItem4nameEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return new QString(self->name());
}

//  void qdesigner_internal::WidgetDataBaseItem::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18WidgetDataBaseItem7setNameERK7QString(
    qdesigner_internal::WidgetDataBaseItem *self,
    const QString *name) {
  self->setName(*name);
}

//  QString qdesigner_internal::WidgetDataBaseItem::group() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal18WidgetDataBaseItem5groupEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return new QString(self->group());
}

//  void qdesigner_internal::WidgetDataBaseItem::setGroup(const QString
//      &group)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18WidgetDataBaseItem8setGroupERK7QString(
    qdesigner_internal::WidgetDataBaseItem *self,
    const QString *group) {
  self->setGroup(*group);
}

//  QString qdesigner_internal::WidgetDataBaseItem::toolTip() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal18WidgetDataBaseItem7toolTipEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return new QString(self->toolTip());
}

//  void qdesigner_internal::WidgetDataBaseItem::setToolTip(const QString
//      &toolTip)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18WidgetDataBaseItem10setToolTipERK7QString(
    qdesigner_internal::WidgetDataBaseItem *self,
    const QString *toolTip) {
  self->setToolTip(*toolTip);
}

//  QString qdesigner_internal::WidgetDataBaseItem::whatsThis() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal18WidgetDataBaseItem9whatsThisEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return new QString(self->whatsThis());
}

//  void qdesigner_internal::WidgetDataBaseItem::setWhatsThis(const QString
//      &whatsThis)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18WidgetDataBaseItem12setWhatsThisERK7QString(
    qdesigner_internal::WidgetDataBaseItem *self,
    const QString *whatsThis) {
  self->setWhatsThis(*whatsThis);
}

//  QString qdesigner_internal::WidgetDataBaseItem::includeFile() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal18WidgetDataBaseItem11includeFileEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return new QString(self->includeFile());
}

//  void qdesigner_internal::WidgetDataBaseItem::setIncludeFile(const QString
//      &includeFile)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18WidgetDataBaseItem14setIncludeFileERK7QString(
    qdesigner_internal::WidgetDataBaseItem *self,
    const QString *includeFile) {
  self->setIncludeFile(*includeFile);
}

//  QIcon qdesigner_internal::WidgetDataBaseItem::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK18qdesigner_internal18WidgetDataBaseItem4iconEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return new QIcon(self->icon());
}

//  void qdesigner_internal::WidgetDataBaseItem::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18WidgetDataBaseItem7setIconERK5QIcon(
    qdesigner_internal::WidgetDataBaseItem *self,
    const QIcon *icon) {
  self->setIcon(*icon);
}

//  bool qdesigner_internal::WidgetDataBaseItem::isCompat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal18WidgetDataBaseItem8isCompatEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return self->isCompat();
}

//  void qdesigner_internal::WidgetDataBaseItem::setCompat(bool compat)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18WidgetDataBaseItem9setCompatEb(
    qdesigner_internal::WidgetDataBaseItem *self,
    bool compat) {
  self->setCompat(compat);
}

//  bool qdesigner_internal::WidgetDataBaseItem::isContainer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal18WidgetDataBaseItem11isContainerEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return self->isContainer();
}

//  void qdesigner_internal::WidgetDataBaseItem::setContainer(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18WidgetDataBaseItem12setContainerEb(
    qdesigner_internal::WidgetDataBaseItem *self,
    bool b) {
  self->setContainer(b);
}

//  bool qdesigner_internal::WidgetDataBaseItem::isCustom() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal18WidgetDataBaseItem8isCustomEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return self->isCustom();
}

//  void qdesigner_internal::WidgetDataBaseItem::setCustom(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18WidgetDataBaseItem9setCustomEb(
    qdesigner_internal::WidgetDataBaseItem *self,
    bool b) {
  self->setCustom(b);
}

//  QString qdesigner_internal::WidgetDataBaseItem::pluginPath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal18WidgetDataBaseItem10pluginPathEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return new QString(self->pluginPath());
}

//  void qdesigner_internal::WidgetDataBaseItem::setPluginPath(const QString
//      &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18WidgetDataBaseItem13setPluginPathERK7QString(
    qdesigner_internal::WidgetDataBaseItem *self,
    const QString *path) {
  self->setPluginPath(*path);
}

//  bool qdesigner_internal::WidgetDataBaseItem::isPromoted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal18WidgetDataBaseItem10isPromotedEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return self->isPromoted();
}

//  void qdesigner_internal::WidgetDataBaseItem::setPromoted(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18WidgetDataBaseItem11setPromotedEb(
    qdesigner_internal::WidgetDataBaseItem *self,
    bool b) {
  self->setPromoted(b);
}

//  QString qdesigner_internal::WidgetDataBaseItem::extends() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal18WidgetDataBaseItem7extendsEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return new QString(self->extends());
}

//  void qdesigner_internal::WidgetDataBaseItem::setExtends(const QString &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18WidgetDataBaseItem10setExtendsERK7QString(
    qdesigner_internal::WidgetDataBaseItem *self,
    const QString *s) {
  self->setExtends(*s);
}

//  void
//      qdesigner_internal::WidgetDataBaseItem::setDefaultPropertyValues(cons
//      t QList<QVariant> &list)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18WidgetDataBaseItem24setDefaultPropertyValuesERK5QListI8QVariantE(
    qdesigner_internal::WidgetDataBaseItem *self,
    const QList<QVariant> *list) {
  self->setDefaultPropertyValues(*list);
}

//  QList<QVariant>
//      qdesigner_internal::WidgetDataBaseItem::defaultPropertyValues() const
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZNK18qdesigner_internal18WidgetDataBaseItem21defaultPropertyValuesEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return new QList<QVariant>(self->defaultPropertyValues());
}

//  WidgetDataBaseItem *qdesigner_internal::WidgetDataBaseItem::clone(const
//      QDesignerWidgetDataBaseItemInterface *item)
extern "C" Q_DECL_EXPORT
qdesigner_internal::WidgetDataBaseItem *ritual_ZN18qdesigner_internal18WidgetDataBaseItem5cloneEPK36QDesignerWidgetDataBaseItemInterface(
    const QDesignerWidgetDataBaseItemInterface *item) {
  return qdesigner_internal::WidgetDataBaseItem::clone(item);
}

//  QString qdesigner_internal::WidgetDataBaseItem::baseClassName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal18WidgetDataBaseItem13baseClassNameEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return new QString(self->baseClassName());
}

//  void qdesigner_internal::WidgetDataBaseItem::setBaseClassName(const
//      QString &b)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18WidgetDataBaseItem16setBaseClassNameERK7QString(
    qdesigner_internal::WidgetDataBaseItem *self,
    const QString *b) {
  self->setBaseClassName(*b);
}

//  QStringList qdesigner_internal::WidgetDataBaseItem::fakeSlots() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18qdesigner_internal18WidgetDataBaseItem9fakeSlotsEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return new QList<QString>(self->fakeSlots());
}

//  void qdesigner_internal::WidgetDataBaseItem::setFakeSlots(const
//      QStringList &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18WidgetDataBaseItem12setFakeSlotsERK5QListI7QStringE(
    qdesigner_internal::WidgetDataBaseItem *self,
    const QList<QString> *a0) {
  self->setFakeSlots(*a0);
}

//  QStringList qdesigner_internal::WidgetDataBaseItem::fakeSignals() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18qdesigner_internal18WidgetDataBaseItem11fakeSignalsEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return new QList<QString>(self->fakeSignals());
}

//  void qdesigner_internal::WidgetDataBaseItem::setFakeSignals(const
//      QStringList &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18WidgetDataBaseItem14setFakeSignalsERK5QListI7QStringE(
    qdesigner_internal::WidgetDataBaseItem *self,
    const QList<QString> *a0) {
  self->setFakeSignals(*a0);
}

//  QString qdesigner_internal::WidgetDataBaseItem::addPageMethod() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal18WidgetDataBaseItem13addPageMethodEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return new QString(self->addPageMethod());
}

//  void qdesigner_internal::WidgetDataBaseItem::setAddPageMethod(const
//      QString &m)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18WidgetDataBaseItem16setAddPageMethodERK7QString(
    qdesigner_internal::WidgetDataBaseItem *self,
    const QString *m) {
  self->setAddPageMethod(*m);
}

//  QString qdesigner_internal::WidgetDataBaseItem::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem4nameEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return new QString(self->qdesigner_internal::WidgetDataBaseItem::name());
}

//  void qdesigner_internal::WidgetDataBaseItem::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem7setNameERK7QString(
    qdesigner_internal::WidgetDataBaseItem *self,
    const QString *name) {
  self->qdesigner_internal::WidgetDataBaseItem::setName(*name);
}

//  QString qdesigner_internal::WidgetDataBaseItem::group() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem5groupEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return new QString(self->qdesigner_internal::WidgetDataBaseItem::group());
}

//  void qdesigner_internal::WidgetDataBaseItem::setGroup(const QString
//      &group)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem8setGroupERK7QString(
    qdesigner_internal::WidgetDataBaseItem *self,
    const QString *group) {
  self->qdesigner_internal::WidgetDataBaseItem::setGroup(*group);
}

//  QString qdesigner_internal::WidgetDataBaseItem::toolTip() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem7toolTipEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return new QString(
      self->qdesigner_internal::WidgetDataBaseItem::toolTip());
}

//  void qdesigner_internal::WidgetDataBaseItem::setToolTip(const QString
//      &toolTip)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem10setToolTipERK7QString(
    qdesigner_internal::WidgetDataBaseItem *self,
    const QString *toolTip) {
  self->qdesigner_internal::WidgetDataBaseItem::setToolTip(*toolTip);
}

//  QString qdesigner_internal::WidgetDataBaseItem::whatsThis() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem9whatsThisEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return new QString(
      self->qdesigner_internal::WidgetDataBaseItem::whatsThis());
}

//  void qdesigner_internal::WidgetDataBaseItem::setWhatsThis(const QString
//      &whatsThis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem12setWhatsThisERK7QString(
    qdesigner_internal::WidgetDataBaseItem *self,
    const QString *whatsThis) {
  self->qdesigner_internal::WidgetDataBaseItem::setWhatsThis(*whatsThis);
}

//  QString qdesigner_internal::WidgetDataBaseItem::includeFile() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem11includeFileEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return new QString(
      self->qdesigner_internal::WidgetDataBaseItem::includeFile());
}

//  void qdesigner_internal::WidgetDataBaseItem::setIncludeFile(const QString
//      &includeFile)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem14setIncludeFileERK7QString(
    qdesigner_internal::WidgetDataBaseItem *self,
    const QString *includeFile) {
  self->qdesigner_internal::WidgetDataBaseItem::setIncludeFile(*includeFile);
}

//  QIcon qdesigner_internal::WidgetDataBaseItem::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem4iconEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return new QIcon(self->qdesigner_internal::WidgetDataBaseItem::icon());
}

//  void qdesigner_internal::WidgetDataBaseItem::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem7setIconERK5QIcon(
    qdesigner_internal::WidgetDataBaseItem *self,
    const QIcon *icon) {
  self->qdesigner_internal::WidgetDataBaseItem::setIcon(*icon);
}

//  bool qdesigner_internal::WidgetDataBaseItem::isCompat() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem8isCompatEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return self->qdesigner_internal::WidgetDataBaseItem::isCompat();
}

//  void qdesigner_internal::WidgetDataBaseItem::setCompat(bool compat)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem9setCompatEb(
    qdesigner_internal::WidgetDataBaseItem *self,
    bool compat) {
  self->qdesigner_internal::WidgetDataBaseItem::setCompat(compat);
}

//  bool qdesigner_internal::WidgetDataBaseItem::isContainer() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem11isContainerEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return self->qdesigner_internal::WidgetDataBaseItem::isContainer();
}

//  void qdesigner_internal::WidgetDataBaseItem::setContainer(bool b)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem12setContainerEb(
    qdesigner_internal::WidgetDataBaseItem *self,
    bool b) {
  self->qdesigner_internal::WidgetDataBaseItem::setContainer(b);
}

//  bool qdesigner_internal::WidgetDataBaseItem::isCustom() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem8isCustomEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return self->qdesigner_internal::WidgetDataBaseItem::isCustom();
}

//  void qdesigner_internal::WidgetDataBaseItem::setCustom(bool b)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem9setCustomEb(
    qdesigner_internal::WidgetDataBaseItem *self,
    bool b) {
  self->qdesigner_internal::WidgetDataBaseItem::setCustom(b);
}

//  QString qdesigner_internal::WidgetDataBaseItem::pluginPath() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem10pluginPathEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return new QString(
      self->qdesigner_internal::WidgetDataBaseItem::pluginPath());
}

//  void qdesigner_internal::WidgetDataBaseItem::setPluginPath(const QString
//      &path)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem13setPluginPathERK7QString(
    qdesigner_internal::WidgetDataBaseItem *self,
    const QString *path) {
  self->qdesigner_internal::WidgetDataBaseItem::setPluginPath(*path);
}

//  bool qdesigner_internal::WidgetDataBaseItem::isPromoted() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem10isPromotedEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return self->qdesigner_internal::WidgetDataBaseItem::isPromoted();
}

//  void qdesigner_internal::WidgetDataBaseItem::setPromoted(bool b)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem11setPromotedEb(
    qdesigner_internal::WidgetDataBaseItem *self,
    bool b) {
  self->qdesigner_internal::WidgetDataBaseItem::setPromoted(b);
}

//  QString qdesigner_internal::WidgetDataBaseItem::extends() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem7extendsEv(
    const qdesigner_internal::WidgetDataBaseItem *self) {
  return new QString(
      self->qdesigner_internal::WidgetDataBaseItem::extends());
}

//  void qdesigner_internal::WidgetDataBaseItem::setExtends(const QString &s)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem10setExtendsERK7QString(
    qdesigner_internal::WidgetDataBaseItem *self,
    const QString *s) {
  self->qdesigner_internal::WidgetDataBaseItem::setExtends(*s);
}
