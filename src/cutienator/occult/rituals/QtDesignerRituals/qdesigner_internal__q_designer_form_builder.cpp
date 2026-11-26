//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_formbuilder_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_formbuilder_p.h>
#include <QtDesigner/6.12.0/QtDesigner/private/deviceprofile_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qicon.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  Only a class built on qdesigner_internal::QDesignerFormBuilder may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct Ownqdesigner_internal_QDesignerFormBuilder : qdesigner_internal::QDesignerFormBuilder {
  using qdesigner_internal::QDesignerFormBuilder::create;
  using qdesigner_internal::QDesignerFormBuilder::createDom;
  using qdesigner_internal::QDesignerFormBuilder::createResources;
  using qdesigner_internal::QDesignerFormBuilder::createWidget;
  using qdesigner_internal::QDesignerFormBuilder::addItem;
  using qdesigner_internal::QDesignerFormBuilder::nameToIcon;
  using qdesigner_internal::QDesignerFormBuilder::nameToPixmap;
  using qdesigner_internal::QDesignerFormBuilder::loadExtraInfo;
};

//  qdesigner_internal::QDesignerFormBuilder::QDesignerFormBuilder(QDesignerF
//      ormEditorInterface *core, const DeviceProfile &deviceProfile)
extern "C" Q_DECL_EXPORT
qdesigner_internal::QDesignerFormBuilder *ritual_ZN18qdesigner_internal20QDesignerFormBuilderC1EP28QDesignerFormEditorInterfaceRKNS_13DeviceProfileE(
    QDesignerFormEditorInterface *core,
    const qdesigner_internal::DeviceProfile *deviceProfile) {
  return new qdesigner_internal::QDesignerFormBuilder(core, *deviceProfile);
}

//  QWidget *qdesigner_internal::QDesignerFormBuilder::createWidget(DomWidget
//      *ui_widget, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN18qdesigner_internal20QDesignerFormBuilder12createWidgetEP9DomWidgetP7QWidget(
    qdesigner_internal::QDesignerFormBuilder *self,
    DomWidget *ui_widget,
    QWidget *parentWidget) {
  return self->createWidget(ui_widget, parentWidget);
}

//  QDesignerFormEditorInterface
//      *qdesigner_internal::QDesignerFormBuilder::core() const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_ZNK18qdesigner_internal20QDesignerFormBuilder4coreEv(
    const qdesigner_internal::QDesignerFormBuilder *self) {
  return self->core();
}

//  QString qdesigner_internal::QDesignerFormBuilder::systemStyle() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal20QDesignerFormBuilder11systemStyleEv(
    const qdesigner_internal::QDesignerFormBuilder *self) {
  return new QString(self->systemStyle());
}

//  QWidget *qdesigner_internal::QDesignerFormBuilder::createPreview(const
//      QDesignerFormWindowInterface *fw, const QString &styleName, const
//      QString &appStyleSheet, const DeviceProfile &deviceProfile, QString
//      *errorMessage)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN18qdesigner_internal20QDesignerFormBuilder13createPreviewEPK28QDesignerFormWindowInterfaceRK7QStringS6_RKNS_13DeviceProfileEPS4_(
    const QDesignerFormWindowInterface *fw,
    const QString *styleName,
    const QString *appStyleSheet,
    const qdesigner_internal::DeviceProfile *deviceProfile,
    QString *errorMessage) {
  return qdesigner_internal::QDesignerFormBuilder::createPreview(
      fw,
      *styleName,
      *appStyleSheet,
      *deviceProfile,
      errorMessage);
}

//  QWidget *qdesigner_internal::QDesignerFormBuilder::createPreview(const
//      QDesignerFormWindowInterface *fw, const QString &styleName)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN18qdesigner_internal20QDesignerFormBuilder13createPreviewEPK28QDesignerFormWindowInterfaceRK7QString(
    const QDesignerFormWindowInterface *fw,
    const QString *styleName) {
  return qdesigner_internal::QDesignerFormBuilder::createPreview(
      fw,
      *styleName);
}

//  QWidget *qdesigner_internal::QDesignerFormBuilder::createPreview(const
//      QDesignerFormWindowInterface *fw, const QString &styleName, const
//      QString &appStyleSheet, QString *errorMessage)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN18qdesigner_internal20QDesignerFormBuilder13createPreviewEPK28QDesignerFormWindowInterfaceRK7QStringS6_PS4_(
    const QDesignerFormWindowInterface *fw,
    const QString *styleName,
    const QString *appStyleSheet,
    QString *errorMessage) {
  return qdesigner_internal::QDesignerFormBuilder::createPreview(
      fw,
      *styleName,
      *appStyleSheet,
      errorMessage);
}

//  QWidget *qdesigner_internal::QDesignerFormBuilder::createPreview(const
//      QDesignerFormWindowInterface *fw, const QString &styleName, const
//      QString &appStyleSheet)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN18qdesigner_internal20QDesignerFormBuilder13createPreviewEPK28QDesignerFormWindowInterfaceRK7QStringS6_(
    const QDesignerFormWindowInterface *fw,
    const QString *styleName,
    const QString *appStyleSheet) {
  return qdesigner_internal::QDesignerFormBuilder::createPreview(
      fw,
      *styleName,
      *appStyleSheet);
}

//  QPixmap
//      qdesigner_internal::QDesignerFormBuilder::createPreviewPixmap(const
//      QDesignerFormWindowInterface *fw, const QString &styleName, const
//      QString &appStyleSheet)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN18qdesigner_internal20QDesignerFormBuilder19createPreviewPixmapEPK28QDesignerFormWindowInterfaceRK7QStringS6_(
    const QDesignerFormWindowInterface *fw,
    const QString *styleName,
    const QString *appStyleSheet) {
  return new QPixmap(
      qdesigner_internal::QDesignerFormBuilder::createPreviewPixmap(
          fw,
          *styleName,
          *appStyleSheet));
}

//  QWidget *qdesigner_internal::QDesignerFormBuilder::create(DomUI *ui,
//      QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN18qdesigner_internal20QDesignerFormBuilder6createEP5DomUIP7QWidget(
    qdesigner_internal::QDesignerFormBuilder *self,
    DomUI *ui,
    QWidget *parentWidget) {
  return self->create(ui, parentWidget);
}

//  DomWidget *qdesigner_internal::QDesignerFormBuilder::createDom(QWidget
//      *widget, DomWidget *ui_parentWidget, bool recursive)
extern "C" Q_DECL_EXPORT
DomWidget *ritual_ZN18qdesigner_internal20QDesignerFormBuilder9createDomEP7QWidgetP9DomWidgetb(
    qdesigner_internal::QDesignerFormBuilder *self,
    QWidget *widget,
    DomWidget *ui_parentWidget,
    bool recursive) {
  return self->createDom(widget, ui_parentWidget, recursive);
}

//  QWidget *qdesigner_internal::QDesignerFormBuilder::create(DomWidget
//      *ui_widget, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN18qdesigner_internal20QDesignerFormBuilder6createEP9DomWidgetP7QWidget(
    qdesigner_internal::QDesignerFormBuilder *self,
    DomWidget *ui_widget,
    QWidget *parentWidget) {
  return self->create(ui_widget, parentWidget);
}

//  QLayout *qdesigner_internal::QDesignerFormBuilder::create(DomLayout
//      *ui_layout, QLayout *layout, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QLayout *ritual_ZN18qdesigner_internal20QDesignerFormBuilder6createEP9DomLayoutP7QLayoutP7QWidget(
    qdesigner_internal::QDesignerFormBuilder *self,
    DomLayout *ui_layout,
    QLayout *layout,
    QWidget *parentWidget) {
  return self->create(ui_layout, layout, parentWidget);
}

//  void
//      qdesigner_internal::QDesignerFormBuilder::createResources(DomResource
//      s *resources)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20QDesignerFormBuilder15createResourcesEP12DomResources(
    qdesigner_internal::QDesignerFormBuilder *self,
    DomResources *resources) {
  self->createResources(resources);
}

//  QWidget *qdesigner_internal::QDesignerFormBuilder::createWidget(const
//      QString &widgetName, QWidget *parentWidget, const QString &name)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN18qdesigner_internal20QDesignerFormBuilder12createWidgetERK7QStringP7QWidgetS3_(
    qdesigner_internal::QDesignerFormBuilder *self,
    const QString *widgetName,
    QWidget *parentWidget,
    const QString *name) {
  return self->createWidget(*widgetName, parentWidget, *name);
}

//  bool qdesigner_internal::QDesignerFormBuilder::addItem(DomWidget
//      *ui_widget, QWidget *widget, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal20QDesignerFormBuilder7addItemEP9DomWidgetP7QWidgetS4_(
    qdesigner_internal::QDesignerFormBuilder *self,
    DomWidget *ui_widget,
    QWidget *widget,
    QWidget *parentWidget) {
  return self->addItem(ui_widget, widget, parentWidget);
}

//  bool qdesigner_internal::QDesignerFormBuilder::addItem(DomLayoutItem
//      *ui_item, QLayoutItem *item, QLayout *layout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal20QDesignerFormBuilder7addItemEP13DomLayoutItemP11QLayoutItemP7QLayout(
    qdesigner_internal::QDesignerFormBuilder *self,
    DomLayoutItem *ui_item,
    QLayoutItem *item,
    QLayout *layout) {
  return self->addItem(ui_item, item, layout);
}

//  QIcon qdesigner_internal::QDesignerFormBuilder::nameToIcon(const QString
//      &filePath, const QString &qrcPath)
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZN18qdesigner_internal20QDesignerFormBuilder10nameToIconERK7QStringS3_(
    qdesigner_internal::QDesignerFormBuilder *self,
    const QString *filePath,
    const QString *qrcPath) {
  return new QIcon(self->nameToIcon(*filePath, *qrcPath));
}

//  QPixmap qdesigner_internal::QDesignerFormBuilder::nameToPixmap(const
//      QString &filePath, const QString &qrcPath)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN18qdesigner_internal20QDesignerFormBuilder12nameToPixmapERK7QStringS3_(
    qdesigner_internal::QDesignerFormBuilder *self,
    const QString *filePath,
    const QString *qrcPath) {
  return new QPixmap(self->nameToPixmap(*filePath, *qrcPath));
}

//  void qdesigner_internal::QDesignerFormBuilder::applyProperties(QObject
//      *o, const QList<DomProperty *> &properties)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20QDesignerFormBuilder15applyPropertiesEP7QObjectRK5QListIP11DomPropertyE(
    qdesigner_internal::QDesignerFormBuilder *self,
    QObject *o,
    const QList<DomProperty *> *properties) {
  self->applyProperties(o, *properties);
}

//  void qdesigner_internal::QDesignerFormBuilder::loadExtraInfo(DomWidget
//      *ui_widget, QWidget *widget, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20QDesignerFormBuilder13loadExtraInfoEP9DomWidgetP7QWidgetS4_(
    qdesigner_internal::QDesignerFormBuilder *self,
    DomWidget *ui_widget,
    QWidget *widget,
    QWidget *parentWidget) {
  self->loadExtraInfo(ui_widget, widget, parentWidget);
}

//  QtResourceSet
//      *qdesigner_internal::QDesignerFormBuilder::internalResourceSet()
//      const
extern "C" Q_DECL_EXPORT
QtResourceSet *ritual_ZNK18qdesigner_internal20QDesignerFormBuilder19internalResourceSetEv(
    const qdesigner_internal::QDesignerFormBuilder *self) {
  return self->internalResourceSet();
}

//  DeviceProfile qdesigner_internal::QDesignerFormBuilder::deviceProfile()
//      const
extern "C" Q_DECL_EXPORT
qdesigner_internal::DeviceProfile *ritual_ZNK18qdesigner_internal20QDesignerFormBuilder13deviceProfileEv(
    const qdesigner_internal::QDesignerFormBuilder *self) {
  return new qdesigner_internal::DeviceProfile(self->deviceProfile());
}

//  QWidget *qdesigner_internal::QDesignerFormBuilder::createWidget(DomWidget
//      *ui_widget, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder12createWidgetEP9DomWidgetP7QWidget(
    qdesigner_internal::QDesignerFormBuilder *self,
    DomWidget *ui_widget,
    QWidget *parentWidget) {
  return self->qdesigner_internal::QDesignerFormBuilder::createWidget(
      ui_widget,
      parentWidget);
}

//  QWidget *qdesigner_internal::QDesignerFormBuilder::create(DomUI *ui,
//      QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder6createEP5DomUIP7QWidget(
    qdesigner_internal::QDesignerFormBuilder *self,
    DomUI *ui,
    QWidget *parentWidget) {
  return static_cast<Ownqdesigner_internal_QDesignerFormBuilder *>(self)->Ownqdesigner_internal_QDesignerFormBuilder::create(
      ui,
      parentWidget);
}

//  DomWidget *qdesigner_internal::QDesignerFormBuilder::createDom(QWidget
//      *widget, DomWidget *ui_parentWidget, bool recursive)
extern "C" Q_DECL_EXPORT
DomWidget *ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder9createDomEP7QWidgetP9DomWidgetb(
    qdesigner_internal::QDesignerFormBuilder *self,
    QWidget *widget,
    DomWidget *ui_parentWidget,
    bool recursive) {
  return static_cast<Ownqdesigner_internal_QDesignerFormBuilder *>(self)->Ownqdesigner_internal_QDesignerFormBuilder::createDom(
      widget,
      ui_parentWidget,
      recursive);
}

//  QWidget *qdesigner_internal::QDesignerFormBuilder::create(DomWidget
//      *ui_widget, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder6createEP9DomWidgetP7QWidget(
    qdesigner_internal::QDesignerFormBuilder *self,
    DomWidget *ui_widget,
    QWidget *parentWidget) {
  return static_cast<Ownqdesigner_internal_QDesignerFormBuilder *>(self)->Ownqdesigner_internal_QDesignerFormBuilder::create(
      ui_widget,
      parentWidget);
}

//  QLayout *qdesigner_internal::QDesignerFormBuilder::create(DomLayout
//      *ui_layout, QLayout *layout, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QLayout *ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder6createEP9DomLayoutP7QLayoutP7QWidget(
    qdesigner_internal::QDesignerFormBuilder *self,
    DomLayout *ui_layout,
    QLayout *layout,
    QWidget *parentWidget) {
  return static_cast<Ownqdesigner_internal_QDesignerFormBuilder *>(self)->Ownqdesigner_internal_QDesignerFormBuilder::create(
      ui_layout,
      layout,
      parentWidget);
}

//  void
//      qdesigner_internal::QDesignerFormBuilder::createResources(DomResource
//      s *resources)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder15createResourcesEP12DomResources(
    qdesigner_internal::QDesignerFormBuilder *self,
    DomResources *resources) {
  static_cast<Ownqdesigner_internal_QDesignerFormBuilder *>(self)->Ownqdesigner_internal_QDesignerFormBuilder::createResources(
      resources);
}

//  QWidget *qdesigner_internal::QDesignerFormBuilder::createWidget(const
//      QString &widgetName, QWidget *parentWidget, const QString &name)
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder12createWidgetERK7QStringP7QWidgetS3_(
    qdesigner_internal::QDesignerFormBuilder *self,
    const QString *widgetName,
    QWidget *parentWidget,
    const QString *name) {
  return static_cast<Ownqdesigner_internal_QDesignerFormBuilder *>(self)->Ownqdesigner_internal_QDesignerFormBuilder::createWidget(
      *widgetName,
      parentWidget,
      *name);
}

//  bool qdesigner_internal::QDesignerFormBuilder::addItem(DomWidget
//      *ui_widget, QWidget *widget, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder7addItemEP9DomWidgetP7QWidgetS4_(
    qdesigner_internal::QDesignerFormBuilder *self,
    DomWidget *ui_widget,
    QWidget *widget,
    QWidget *parentWidget) {
  return static_cast<Ownqdesigner_internal_QDesignerFormBuilder *>(self)->Ownqdesigner_internal_QDesignerFormBuilder::addItem(
      ui_widget,
      widget,
      parentWidget);
}

//  bool qdesigner_internal::QDesignerFormBuilder::addItem(DomLayoutItem
//      *ui_item, QLayoutItem *item, QLayout *layout)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder7addItemEP13DomLayoutItemP11QLayoutItemP7QLayout(
    qdesigner_internal::QDesignerFormBuilder *self,
    DomLayoutItem *ui_item,
    QLayoutItem *item,
    QLayout *layout) {
  return static_cast<Ownqdesigner_internal_QDesignerFormBuilder *>(self)->Ownqdesigner_internal_QDesignerFormBuilder::addItem(
      ui_item,
      item,
      layout);
}

//  QIcon qdesigner_internal::QDesignerFormBuilder::nameToIcon(const QString
//      &filePath, const QString &qrcPath)
extern "C" Q_DECL_EXPORT
QIcon *ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder10nameToIconERK7QStringS3_(
    qdesigner_internal::QDesignerFormBuilder *self,
    const QString *filePath,
    const QString *qrcPath) {
  return new QIcon(
      static_cast<Ownqdesigner_internal_QDesignerFormBuilder *>(self)->Ownqdesigner_internal_QDesignerFormBuilder::nameToIcon(
          *filePath,
          *qrcPath));
}

//  QPixmap qdesigner_internal::QDesignerFormBuilder::nameToPixmap(const
//      QString &filePath, const QString &qrcPath)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder12nameToPixmapERK7QStringS3_(
    qdesigner_internal::QDesignerFormBuilder *self,
    const QString *filePath,
    const QString *qrcPath) {
  return new QPixmap(
      static_cast<Ownqdesigner_internal_QDesignerFormBuilder *>(self)->Ownqdesigner_internal_QDesignerFormBuilder::nameToPixmap(
          *filePath,
          *qrcPath));
}

//  void qdesigner_internal::QDesignerFormBuilder::loadExtraInfo(DomWidget
//      *ui_widget, QWidget *widget, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder13loadExtraInfoEP9DomWidgetP7QWidgetS4_(
    qdesigner_internal::QDesignerFormBuilder *self,
    DomWidget *ui_widget,
    QWidget *widget,
    QWidget *parentWidget) {
  static_cast<Ownqdesigner_internal_QDesignerFormBuilder *>(self)->Ownqdesigner_internal_QDesignerFormBuilder::loadExtraInfo(
      ui_widget,
      widget,
      parentWidget);
}
