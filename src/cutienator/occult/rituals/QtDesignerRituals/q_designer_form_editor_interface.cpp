//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractformeditor.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/abstractformeditor.h>
#include <QtCore/qstring.h>
#include <QtDesigner/abstractoptionspage.h>
#include <QtCore/qobject.h>
#include <QtGui/qicon.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDesignerFormEditorInterface that Python can take functions over in. Every QDesignerFormEditorInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerFormEditorInterfaceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerFormEditorInterfaceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerFormEditorInterfaceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerFormEditorInterfaceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerFormEditorInterfaceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerFormEditorInterfaceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerFormEditorInterfaceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerFormEditorInterface : public QDesignerFormEditorInterface {
public:
  using QDesignerFormEditorInterface::QDesignerFormEditorInterface;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerFormEditorInterfaceCall0 call = reinterpret_cast<CuteQDesignerFormEditorInterfaceCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerFormEditorInterfaceCall1 call = reinterpret_cast<CuteQDesignerFormEditorInterfaceCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerFormEditorInterfaceCall2 call = reinterpret_cast<CuteQDesignerFormEditorInterfaceCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerFormEditorInterfaceCall3 call = reinterpret_cast<CuteQDesignerFormEditorInterfaceCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerFormEditorInterfaceCall4 call = reinterpret_cast<CuteQDesignerFormEditorInterfaceCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerFormEditorInterfaceCall5 call = reinterpret_cast<CuteQDesignerFormEditorInterfaceCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerFormEditorInterfaceCall6 call = reinterpret_cast<CuteQDesignerFormEditorInterfaceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerFormEditorInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QDesignerFormEditorInterface10metaObjectEv(
    const QDesignerFormEditorInterface *self) {
  return self->metaObject();
}

//  void *QDesignerFormEditorInterface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QDesignerFormEditorInterface11qt_metacastEPKc(
    QDesignerFormEditorInterface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDesignerFormEditorInterface::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QDesignerFormEditorInterface11qt_metacallEN11QMetaObject4CallEiPPv(
    QDesignerFormEditorInterface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDesignerFormEditorInterface::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QDesignerFormEditorInterface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerFormEditorInterface::tr(s, c, n));
}

//  QDesignerFormEditorInterface::QDesignerFormEditorInterface(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_ZN28QDesignerFormEditorInterfaceC1EP7QObject(
    QObject *parent) {
  return new CuteQDesignerFormEditorInterface(parent);
}

//  QDesignerFormEditorInterface::~QDesignerFormEditorInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormEditorInterfaceD1Ev(
    QDesignerFormEditorInterface *self) {
  delete self;
}

//  QExtensionManager *QDesignerFormEditorInterface::extensionManager() const
extern "C" Q_DECL_EXPORT
QExtensionManager *ritual_ZNK28QDesignerFormEditorInterface16extensionManagerEv(
    const QDesignerFormEditorInterface *self) {
  return self->extensionManager();
}

//  QWidget *QDesignerFormEditorInterface::topLevel() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK28QDesignerFormEditorInterface8topLevelEv(
    const QDesignerFormEditorInterface *self) {
  return self->topLevel();
}

//  QDesignerWidgetBoxInterface *QDesignerFormEditorInterface::widgetBox()
//      const
extern "C" Q_DECL_EXPORT
QDesignerWidgetBoxInterface *ritual_ZNK28QDesignerFormEditorInterface9widgetBoxEv(
    const QDesignerFormEditorInterface *self) {
  return self->widgetBox();
}

//  QDesignerPropertyEditorInterface
//      *QDesignerFormEditorInterface::propertyEditor() const
extern "C" Q_DECL_EXPORT
QDesignerPropertyEditorInterface *ritual_ZNK28QDesignerFormEditorInterface14propertyEditorEv(
    const QDesignerFormEditorInterface *self) {
  return self->propertyEditor();
}

//  QDesignerObjectInspectorInterface
//      *QDesignerFormEditorInterface::objectInspector() const
extern "C" Q_DECL_EXPORT
QDesignerObjectInspectorInterface *ritual_ZNK28QDesignerFormEditorInterface15objectInspectorEv(
    const QDesignerFormEditorInterface *self) {
  return self->objectInspector();
}

//  QDesignerFormWindowManagerInterface
//      *QDesignerFormEditorInterface::formWindowManager() const
extern "C" Q_DECL_EXPORT
QDesignerFormWindowManagerInterface *ritual_ZNK28QDesignerFormEditorInterface17formWindowManagerEv(
    const QDesignerFormEditorInterface *self) {
  return self->formWindowManager();
}

//  QDesignerWidgetDataBaseInterface
//      *QDesignerFormEditorInterface::widgetDataBase() const
extern "C" Q_DECL_EXPORT
QDesignerWidgetDataBaseInterface *ritual_ZNK28QDesignerFormEditorInterface14widgetDataBaseEv(
    const QDesignerFormEditorInterface *self) {
  return self->widgetDataBase();
}

//  QDesignerMetaDataBaseInterface
//      *QDesignerFormEditorInterface::metaDataBase() const
extern "C" Q_DECL_EXPORT
QDesignerMetaDataBaseInterface *ritual_ZNK28QDesignerFormEditorInterface12metaDataBaseEv(
    const QDesignerFormEditorInterface *self) {
  return self->metaDataBase();
}

//  QDesignerPromotionInterface *QDesignerFormEditorInterface::promotion()
//      const
extern "C" Q_DECL_EXPORT
QDesignerPromotionInterface *ritual_ZNK28QDesignerFormEditorInterface9promotionEv(
    const QDesignerFormEditorInterface *self) {
  return self->promotion();
}

//  QDesignerWidgetFactoryInterface
//      *QDesignerFormEditorInterface::widgetFactory() const
extern "C" Q_DECL_EXPORT
QDesignerWidgetFactoryInterface *ritual_ZNK28QDesignerFormEditorInterface13widgetFactoryEv(
    const QDesignerFormEditorInterface *self) {
  return self->widgetFactory();
}

//  QDesignerActionEditorInterface
//      *QDesignerFormEditorInterface::actionEditor() const
extern "C" Q_DECL_EXPORT
QDesignerActionEditorInterface *ritual_ZNK28QDesignerFormEditorInterface12actionEditorEv(
    const QDesignerFormEditorInterface *self) {
  return self->actionEditor();
}

//  QDesignerIntegrationInterface
//      *QDesignerFormEditorInterface::integration() const
extern "C" Q_DECL_EXPORT
QDesignerIntegrationInterface *ritual_ZNK28QDesignerFormEditorInterface11integrationEv(
    const QDesignerFormEditorInterface *self) {
  return self->integration();
}

//  QDesignerPluginManager *QDesignerFormEditorInterface::pluginManager()
//      const
extern "C" Q_DECL_EXPORT
QDesignerPluginManager *ritual_ZNK28QDesignerFormEditorInterface13pluginManagerEv(
    const QDesignerFormEditorInterface *self) {
  return self->pluginManager();
}

//  QDesignerIntrospectionInterface
//      *QDesignerFormEditorInterface::introspection() const
extern "C" Q_DECL_EXPORT
QDesignerIntrospectionInterface *ritual_ZNK28QDesignerFormEditorInterface13introspectionEv(
    const QDesignerFormEditorInterface *self) {
  return self->introspection();
}

//  QDesignerDialogGuiInterface *QDesignerFormEditorInterface::dialogGui()
//      const
extern "C" Q_DECL_EXPORT
QDesignerDialogGuiInterface *ritual_ZNK28QDesignerFormEditorInterface9dialogGuiEv(
    const QDesignerFormEditorInterface *self) {
  return self->dialogGui();
}

//  QDesignerSettingsInterface
//      *QDesignerFormEditorInterface::settingsManager() const
extern "C" Q_DECL_EXPORT
QDesignerSettingsInterface *ritual_ZNK28QDesignerFormEditorInterface15settingsManagerEv(
    const QDesignerFormEditorInterface *self) {
  return self->settingsManager();
}

//  QString QDesignerFormEditorInterface::resourceLocation() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QDesignerFormEditorInterface16resourceLocationEv(
    const QDesignerFormEditorInterface *self) {
  return new QString(self->resourceLocation());
}

//  QtResourceModel *QDesignerFormEditorInterface::resourceModel() const
extern "C" Q_DECL_EXPORT
QtResourceModel *ritual_ZNK28QDesignerFormEditorInterface13resourceModelEv(
    const QDesignerFormEditorInterface *self) {
  return self->resourceModel();
}

//  QtGradientManager *QDesignerFormEditorInterface::gradientManager() const
extern "C" Q_DECL_EXPORT
QtGradientManager *ritual_ZNK28QDesignerFormEditorInterface15gradientManagerEv(
    const QDesignerFormEditorInterface *self) {
  return self->gradientManager();
}

//  QList<QDesignerOptionsPageInterface *>
//      QDesignerFormEditorInterface::optionsPages() const
extern "C" Q_DECL_EXPORT
QList<QDesignerOptionsPageInterface *> *ritual_ZNK28QDesignerFormEditorInterface12optionsPagesEv(
    const QDesignerFormEditorInterface *self) {
  return new QList<QDesignerOptionsPageInterface *>(self->optionsPages());
}

//  void QDesignerFormEditorInterface::setTopLevel(QWidget *topLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormEditorInterface11setTopLevelEP7QWidget(
    QDesignerFormEditorInterface *self,
    QWidget *topLevel) {
  self->setTopLevel(topLevel);
}

//  void
//      QDesignerFormEditorInterface::setWidgetBox(QDesignerWidgetBoxInterfac
//      e *widgetBox)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormEditorInterface12setWidgetBoxEP27QDesignerWidgetBoxInterface(
    QDesignerFormEditorInterface *self,
    QDesignerWidgetBoxInterface *widgetBox) {
  self->setWidgetBox(widgetBox);
}

//  void QDesignerFormEditorInterface::setPropertyEditor(QDesignerPropertyEdi
//      torInterface *propertyEditor)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormEditorInterface17setPropertyEditorEP32QDesignerPropertyEditorInterface(
    QDesignerFormEditorInterface *self,
    QDesignerPropertyEditorInterface *propertyEditor) {
  self->setPropertyEditor(propertyEditor);
}

//  void QDesignerFormEditorInterface::setObjectInspector(QDesignerObjectInsp
//      ectorInterface *objectInspector)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormEditorInterface18setObjectInspectorEP33QDesignerObjectInspectorInterface(
    QDesignerFormEditorInterface *self,
    QDesignerObjectInspectorInterface *objectInspector) {
  self->setObjectInspector(objectInspector);
}

//  void
//      QDesignerFormEditorInterface::setPluginManager(QDesignerPluginManager
//      *pluginManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormEditorInterface16setPluginManagerEP22QDesignerPluginManager(
    QDesignerFormEditorInterface *self,
    QDesignerPluginManager *pluginManager) {
  self->setPluginManager(pluginManager);
}

//  void QDesignerFormEditorInterface::setActionEditor(QDesignerActionEditorI
//      nterface *actionEditor)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormEditorInterface15setActionEditorEP30QDesignerActionEditorInterface(
    QDesignerFormEditorInterface *self,
    QDesignerActionEditorInterface *actionEditor) {
  self->setActionEditor(actionEditor);
}

//  void QDesignerFormEditorInterface::setIntegration(QDesignerIntegrationInt
//      erface *integration)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormEditorInterface14setIntegrationEP29QDesignerIntegrationInterface(
    QDesignerFormEditorInterface *self,
    QDesignerIntegrationInterface *integration) {
  self->setIntegration(integration);
}

//  void QDesignerFormEditorInterface::setIntrospection(QDesignerIntrospectio
//      nInterface *introspection)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormEditorInterface16setIntrospectionEP31QDesignerIntrospectionInterface(
    QDesignerFormEditorInterface *self,
    QDesignerIntrospectionInterface *introspection) {
  self->setIntrospection(introspection);
}

//  void
//      QDesignerFormEditorInterface::setDialogGui(QDesignerDialogGuiInterfac
//      e *dialogGui)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormEditorInterface12setDialogGuiEP27QDesignerDialogGuiInterface(
    QDesignerFormEditorInterface *self,
    QDesignerDialogGuiInterface *dialogGui) {
  self->setDialogGui(dialogGui);
}

//  void QDesignerFormEditorInterface::setSettingsManager(QDesignerSettingsIn
//      terface *settingsManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormEditorInterface18setSettingsManagerEP26QDesignerSettingsInterface(
    QDesignerFormEditorInterface *self,
    QDesignerSettingsInterface *settingsManager) {
  self->setSettingsManager(settingsManager);
}

//  void QDesignerFormEditorInterface::setResourceModel(QtResourceModel
//      *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormEditorInterface16setResourceModelEP15QtResourceModel(
    QDesignerFormEditorInterface *self,
    QtResourceModel *model) {
  self->setResourceModel(model);
}

//  void QDesignerFormEditorInterface::setGradientManager(QtGradientManager
//      *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormEditorInterface18setGradientManagerEP17QtGradientManager(
    QDesignerFormEditorInterface *self,
    QtGradientManager *manager) {
  self->setGradientManager(manager);
}

//  void QDesignerFormEditorInterface::setOptionsPages(const
//      QList<QDesignerOptionsPageInterface *> &optionsPages)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormEditorInterface15setOptionsPagesERK5QListIP29QDesignerOptionsPageInterfaceE(
    QDesignerFormEditorInterface *self,
    const QList<QDesignerOptionsPageInterface *> *optionsPages) {
  self->setOptionsPages(*optionsPages);
}

//  QObjectList QDesignerFormEditorInterface::pluginInstances() const
extern "C" Q_DECL_EXPORT
QList<QObject *> *ritual_ZNK28QDesignerFormEditorInterface15pluginInstancesEv(
    const QDesignerFormEditorInterface *self) {
  return new QList<QObject *>(self->pluginInstances());
}

//  QIcon QDesignerFormEditorInterface::createIcon(const QString &name)
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZN28QDesignerFormEditorInterface10createIconERK7QString(
    const QString *name) {
  return new QIcon(QDesignerFormEditorInterface::createIcon(*name));
}

//  void QDesignerFormEditorInterface::setFormManager(QDesignerFormWindowMana
//      gerInterface *formWindowManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormEditorInterface14setFormManagerEP35QDesignerFormWindowManagerInterface(
    QDesignerFormEditorInterface *self,
    QDesignerFormWindowManagerInterface *formWindowManager) {
  self->setFormManager(formWindowManager);
}

//  void QDesignerFormEditorInterface::setMetaDataBase(QDesignerMetaDataBaseI
//      nterface *metaDataBase)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormEditorInterface15setMetaDataBaseEP30QDesignerMetaDataBaseInterface(
    QDesignerFormEditorInterface *self,
    QDesignerMetaDataBaseInterface *metaDataBase) {
  self->setMetaDataBase(metaDataBase);
}

//  void QDesignerFormEditorInterface::setWidgetDataBase(QDesignerWidgetDataB
//      aseInterface *widgetDataBase)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormEditorInterface17setWidgetDataBaseEP32QDesignerWidgetDataBaseInterface(
    QDesignerFormEditorInterface *self,
    QDesignerWidgetDataBaseInterface *widgetDataBase) {
  self->setWidgetDataBase(widgetDataBase);
}

//  void
//      QDesignerFormEditorInterface::setPromotion(QDesignerPromotionInterfac
//      e *promotion)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormEditorInterface12setPromotionEP27QDesignerPromotionInterface(
    QDesignerFormEditorInterface *self,
    QDesignerPromotionInterface *promotion) {
  self->setPromotion(promotion);
}

//  void QDesignerFormEditorInterface::setWidgetFactory(QDesignerWidgetFactor
//      yInterface *widgetFactory)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormEditorInterface16setWidgetFactoryEP31QDesignerWidgetFactoryInterface(
    QDesignerFormEditorInterface *self,
    QDesignerWidgetFactoryInterface *widgetFactory) {
  self->setWidgetFactory(widgetFactory);
}

//  void QDesignerFormEditorInterface::setExtensionManager(QExtensionManager
//      *extensionManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormEditorInterface19setExtensionManagerEP17QExtensionManager(
    QDesignerFormEditorInterface *self,
    QExtensionManager *extensionManager) {
  self->setExtensionManager(extensionManager);
}

//  a Python function taken by a CuteQDesignerFormEditorInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerFormEditorInterface(
    QDesignerFormEditorInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerFormEditorInterface *>(self)->take(key, call);
}
