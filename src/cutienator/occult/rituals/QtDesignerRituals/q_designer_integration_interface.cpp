//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractintegration.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/abstractintegration.h>
#include <QtCore/qstring.h>
#include <QtCore/qversionnumber.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDesignerIntegrationInterface that Python can take functions over in. Every QDesignerIntegrationInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQDesignerIntegrationInterfaceCall0)(const void *, QWidget *, int *);
typedef void * (*CuteQDesignerIntegrationInterfaceCall1)(const void *, QWidget *, int *);
typedef QString * (*CuteQDesignerIntegrationInterfaceCall2)(const void *, int *);
typedef void (*CuteQDesignerIntegrationInterfaceCall3)(const void *, const QString *, int *);
typedef bool (*CuteQDesignerIntegrationInterfaceCall4)(const void *, int *);
typedef void (*CuteQDesignerIntegrationInterfaceCall5)(const void *, bool, int *);
typedef int (*CuteQDesignerIntegrationInterfaceCall6)(const void *, int *);
typedef int (*CuteQDesignerIntegrationInterfaceCall7)(const void *, int *);
typedef void (*CuteQDesignerIntegrationInterfaceCall8)(const void *, int, int *);
typedef QString * (*CuteQDesignerIntegrationInterfaceCall9)(const void *, int *);
typedef void (*CuteQDesignerIntegrationInterfaceCall10)(const void *, int, int *);
typedef void (*CuteQDesignerIntegrationInterfaceCall11)(const void *, const QString *, const QVariant *, bool, int *);
typedef void (*CuteQDesignerIntegrationInterfaceCall12)(const void *, const QString *, const QVariant *, int *);
typedef void (*CuteQDesignerIntegrationInterfaceCall13)(const void *, const QString *, int *);
typedef void (*CuteQDesignerIntegrationInterfaceCall14)(const void *, const QString *, const QVariant *, int *);
typedef void (*CuteQDesignerIntegrationInterfaceCall15)(const void *, const QString *, int *);
typedef void (*CuteQDesignerIntegrationInterfaceCall16)(const void *, QDesignerFormWindowInterface *, int *);
typedef void (*CuteQDesignerIntegrationInterfaceCall17)(const void *, QDesignerFormWindowInterface *, int *);
typedef void (*CuteQDesignerIntegrationInterfaceCall18)(const void *, int *);
typedef void (*CuteQDesignerIntegrationInterfaceCall19)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerIntegrationInterfaceCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerIntegrationInterfaceCall21)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerIntegrationInterfaceCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerIntegrationInterfaceCall23)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerIntegrationInterfaceCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerIntegrationInterfaceCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerIntegrationInterfaceCall26)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerIntegrationInterface : public QDesignerIntegrationInterface {
public:
  using QDesignerIntegrationInterface::QDesignerIntegrationInterface;
  void *taken[27] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK29QDesignerIntegrationInterface15containerWindowEP7QWidget")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface21createResourceBrowserEP7QWidget")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QDesignerIntegrationInterface12headerSuffixEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface15setHeaderSuffixERK7QString")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QDesignerIntegrationInterface17isHeaderLowercaseEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface18setHeaderLowercaseEb")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QDesignerIntegrationInterface8featuresEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QDesignerIntegrationInterface28resourceFileWatcherBehaviourEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface31setResourceFileWatcherBehaviourENS_28ResourceFileWatcherBehaviourE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QDesignerIntegrationInterface13contextHelpIdEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface11setFeaturesE6QFlagsINS_11FeatureFlagEE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface14updatePropertyERK7QStringRK8QVariantb")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface14updatePropertyERK7QStringRK8QVariant")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface13resetPropertyERK7QString")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface18addDynamicPropertyERK7QStringRK8QVariant")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface21removeDynamicPropertyERK7QString")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface22updateActiveFormWindowEP28QDesignerFormWindowInterface")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface15setupFormWindowEP28QDesignerFormWindowInterface")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface15updateSelectionEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface25updateCustomWidgetPluginsEv")) {
      taken[19] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QWidget *QDesignerIntegrationInterface::containerWindow(QWidget
  //      *widget) const
  QWidget *containerWindow(QWidget *widget) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall0 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall0>(taken[0]);
      void * given = call(this, widget, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }

  //  QDesignerResourceBrowserInterface
  //      *QDesignerIntegrationInterface::createResourceBrowser(QWidget
  //      *parent)
  QDesignerResourceBrowserInterface *createResourceBrowser(
      QWidget *parent) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall1 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall1>(taken[1]);
      void * given = call(this, parent, &handled);
      if (handled) return static_cast<QDesignerResourceBrowserInterface *>(given);
    }
    return {};
  }

  //  QString QDesignerIntegrationInterface::headerSuffix() const
  QString headerSuffix() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall2 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QDesignerIntegrationInterface::setHeaderSuffix(const QString
  //      &headerSuffix)
  void setHeaderSuffix(const QString &headerSuffix) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall3 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall3>(taken[3]);
      call(this, &headerSuffix, &handled);
      if (handled) return;
    }
  }

  //  bool QDesignerIntegrationInterface::isHeaderLowercase() const
  bool isHeaderLowercase() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall4 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerIntegrationInterface::setHeaderLowercase(bool
  //      headerLowerCase)
  void setHeaderLowercase(bool headerLowerCase) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall5 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall5>(taken[5]);
      call(this, headerLowerCase, &handled);
      if (handled) return;
    }
  }

  //  Feature QDesignerIntegrationInterface::features() const
  QDesignerIntegrationInterface::Feature features() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall6 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return QFlags<QDesignerIntegrationInterface::FeatureFlag>::fromInt(given);
    }
    return {};
  }

  //  ResourceFileWatcherBehaviour
  //      QDesignerIntegrationInterface::resourceFileWatcherBehaviour()
  //      const
  QDesignerIntegrationInterface::ResourceFileWatcherBehaviour resourceFileWatcherBehaviour() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall7 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return static_cast<QDesignerIntegrationInterface::ResourceFileWatcherBehaviour>(given);
    }
    return {};
  }

  //  void QDesignerIntegrationInterface::setResourceFileWatcherBehaviour(R
  //      esourceFileWatcherBehaviour behaviour)
  void setResourceFileWatcherBehaviour(
      QDesignerIntegrationInterface::ResourceFileWatcherBehaviour behaviour) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall8 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall8>(taken[8]);
      call(this, static_cast<int>(behaviour), &handled);
      if (handled) return;
    }
  }

  //  QString QDesignerIntegrationInterface::contextHelpId() const
  QString contextHelpId() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall9 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall9>(taken[9]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QDesignerIntegrationInterface::setFeatures(Feature f)
  void setFeatures(QDesignerIntegrationInterface::Feature f) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall10 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall10>(taken[10]);
      call(this, static_cast<int>(f.toInt()), &handled);
      if (handled) return;
    }
  }

  //  void QDesignerIntegrationInterface::updateProperty(const QString
  //      &name, const QVariant &value, bool enableSubPropertyHandling)
  void updateProperty(
      const QString &name,
      const QVariant &value,
      bool enableSubPropertyHandling) override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall11 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall11>(taken[11]);
      call(this, &name, &value, enableSubPropertyHandling, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerIntegrationInterface::updateProperty(const QString
  //      &name, const QVariant &value)
  void updateProperty(const QString &name, const QVariant &value) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall12 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall12>(taken[12]);
      call(this, &name, &value, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerIntegrationInterface::resetProperty(const QString
  //      &name)
  void resetProperty(const QString &name) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall13 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall13>(taken[13]);
      call(this, &name, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerIntegrationInterface::addDynamicProperty(const QString
  //      &name, const QVariant &value)
  void addDynamicProperty(
      const QString &name,
      const QVariant &value) override {
    if (taken[14]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall14 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall14>(taken[14]);
      call(this, &name, &value, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerIntegrationInterface::removeDynamicProperty(const
  //      QString &name)
  void removeDynamicProperty(const QString &name) override {
    if (taken[15]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall15 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall15>(taken[15]);
      call(this, &name, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerIntegrationInterface::updateActiveFormWindow(QDesignerF
  //      ormWindowInterface *formWindow)
  void updateActiveFormWindow(
      QDesignerFormWindowInterface *formWindow) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall16 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall16>(taken[16]);
      call(this, formWindow, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerIntegrationInterface::setupFormWindow(QDesignerFormWind
  //      owInterface *formWindow)
  void setupFormWindow(QDesignerFormWindowInterface *formWindow) override {
    if (taken[17]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall17 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall17>(taken[17]);
      call(this, formWindow, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerIntegrationInterface::updateSelection()
  void updateSelection() override {
    if (taken[18]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall18 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerIntegrationInterface::updateCustomWidgetPlugins()
  void updateCustomWidgetPlugins() override {
    if (taken[19]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall19 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall20 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall20>(taken[20]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall21 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall21>(taken[21]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall22 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall23 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall24 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall25 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall25>(taken[25]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDesignerIntegrationInterfaceCall26 call = reinterpret_cast<CuteQDesignerIntegrationInterfaceCall26>(taken[26]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerIntegrationInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QDesignerIntegrationInterface10metaObjectEv(
    const QDesignerIntegrationInterface *self) {
  return self->metaObject();
}

//  void *QDesignerIntegrationInterface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN29QDesignerIntegrationInterface11qt_metacastEPKc(
    QDesignerIntegrationInterface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDesignerIntegrationInterface::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN29QDesignerIntegrationInterface11qt_metacallEN11QMetaObject4CallEiPPv(
    QDesignerIntegrationInterface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDesignerIntegrationInterface::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QDesignerIntegrationInterface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerIntegrationInterface::tr(s, c, n));
}

//  QDesignerIntegrationInterface::QDesignerIntegrationInterface(QDesignerFor
//      mEditorInterface *core, QObject *parent)
extern "C" Q_DECL_EXPORT
QDesignerIntegrationInterface *ritual_ZN29QDesignerIntegrationInterfaceC1EP28QDesignerFormEditorInterfaceP7QObject(
    QDesignerFormEditorInterface *core,
    QObject *parent) {
  return new CuteQDesignerIntegrationInterface(core, parent);
}

//  QDesignerIntegrationInterface::~QDesignerIntegrationInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterfaceD1Ev(
    QDesignerIntegrationInterface *self) {
  delete self;
}

//  QDesignerFormEditorInterface *QDesignerIntegrationInterface::core() const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_ZNK29QDesignerIntegrationInterface4coreEv(
    const QDesignerIntegrationInterface *self) {
  return self->core();
}

//  QWidget *QDesignerIntegrationInterface::containerWindow(QWidget *widget)
//      const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK29QDesignerIntegrationInterface15containerWindowEP7QWidget(
    const QDesignerIntegrationInterface *self,
    QWidget *widget) {
  return self->containerWindow(widget);
}

//  QDesignerResourceBrowserInterface
//      *QDesignerIntegrationInterface::createResourceBrowser(QWidget
//      *parent)
extern "C" Q_DECL_EXPORT
QDesignerResourceBrowserInterface *ritual_ZN29QDesignerIntegrationInterface21createResourceBrowserEP7QWidget(
    QDesignerIntegrationInterface *self,
    QWidget *parent) {
  return self->createResourceBrowser(parent);
}

//  QString QDesignerIntegrationInterface::headerSuffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QDesignerIntegrationInterface12headerSuffixEv(
    const QDesignerIntegrationInterface *self) {
  return new QString(self->headerSuffix());
}

//  void QDesignerIntegrationInterface::setHeaderSuffix(const QString
//      &headerSuffix)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface15setHeaderSuffixERK7QString(
    QDesignerIntegrationInterface *self,
    const QString *headerSuffix) {
  self->setHeaderSuffix(*headerSuffix);
}

//  bool QDesignerIntegrationInterface::isHeaderLowercase() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QDesignerIntegrationInterface17isHeaderLowercaseEv(
    const QDesignerIntegrationInterface *self) {
  return self->isHeaderLowercase();
}

//  void QDesignerIntegrationInterface::setHeaderLowercase(bool
//      headerLowerCase)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface18setHeaderLowercaseEb(
    QDesignerIntegrationInterface *self,
    bool headerLowerCase) {
  self->setHeaderLowercase(headerLowerCase);
}

//  QVersionNumber QDesignerIntegrationInterface::qtVersion() const
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZNK29QDesignerIntegrationInterface9qtVersionEv(
    const QDesignerIntegrationInterface *self) {
  return new QVersionNumber(self->qtVersion());
}

//  void QDesignerIntegrationInterface::setQtVersion(const QVersionNumber
//      &qtVersion)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface12setQtVersionERK14QVersionNumber(
    QDesignerIntegrationInterface *self,
    const QVersionNumber *qtVersion) {
  self->setQtVersion(*qtVersion);
}

//  Feature QDesignerIntegrationInterface::features() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QDesignerIntegrationInterface8featuresEv(
    const QDesignerIntegrationInterface *self) {
  return static_cast<int>(self->features().toInt());
}

//  bool QDesignerIntegrationInterface::hasFeature(Feature f) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QDesignerIntegrationInterface10hasFeatureE6QFlagsINS_11FeatureFlagEE(
    const QDesignerIntegrationInterface *self,
    int f) {
  return self->hasFeature(
      QFlags<QDesignerIntegrationInterface::FeatureFlag>::fromInt(f));
}

//  ResourceFileWatcherBehaviour
//      QDesignerIntegrationInterface::resourceFileWatcherBehaviour() const
extern "C" Q_DECL_EXPORT
QDesignerIntegrationInterface::ResourceFileWatcherBehaviour ritual_ZNK29QDesignerIntegrationInterface28resourceFileWatcherBehaviourEv(
    const QDesignerIntegrationInterface *self) {
  return self->resourceFileWatcherBehaviour();
}

//  void QDesignerIntegrationInterface::setResourceFileWatcherBehaviour(Resou
//      rceFileWatcherBehaviour behaviour)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface31setResourceFileWatcherBehaviourENS_28ResourceFileWatcherBehaviourE(
    QDesignerIntegrationInterface *self,
    QDesignerIntegrationInterface::ResourceFileWatcherBehaviour behaviour) {
  self->setResourceFileWatcherBehaviour(behaviour);
}

//  QString QDesignerIntegrationInterface::contextHelpId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QDesignerIntegrationInterface13contextHelpIdEv(
    const QDesignerIntegrationInterface *self) {
  return new QString(self->contextHelpId());
}

//  void QDesignerIntegrationInterface::emitObjectNameChanged(QDesignerFormWi
//      ndowInterface *formWindow, QObject *object, const QString &newName,
//      const QString &oldName)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface21emitObjectNameChangedEP28QDesignerFormWindowInterfaceP7QObjectRK7QStringS6_(
    QDesignerIntegrationInterface *self,
    QDesignerFormWindowInterface *formWindow,
    QObject *object,
    const QString *newName,
    const QString *oldName) {
  self->emitObjectNameChanged(formWindow, object, *newName, *oldName);
}

//  void QDesignerIntegrationInterface::emitNavigateToSlot(const QString
//      &objectName, const QString &signalSignature, const QStringList
//      &parameterNames)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface18emitNavigateToSlotERK7QStringS2_RK5QListIS0_E(
    QDesignerIntegrationInterface *self,
    const QString *objectName,
    const QString *signalSignature,
    const QList<QString> *parameterNames) {
  self->emitNavigateToSlot(*objectName, *signalSignature, *parameterNames);
}

//  void QDesignerIntegrationInterface::emitNavigateToSlot(const QString
//      &slotSignature)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface18emitNavigateToSlotERK7QString(
    QDesignerIntegrationInterface *self,
    const QString *slotSignature) {
  self->emitNavigateToSlot(*slotSignature);
}

//  void QDesignerIntegrationInterface::emitHelpRequested(const QString
//      &manual, const QString &document)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface17emitHelpRequestedERK7QStringS2_(
    QDesignerIntegrationInterface *self,
    const QString *manual,
    const QString *document) {
  self->emitHelpRequested(*manual, *document);
}

//  void QDesignerIntegrationInterface::propertyChanged(QDesignerFormWindowIn
//      terface *formWindow, const QString &name, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface15propertyChangedEP28QDesignerFormWindowInterfaceRK7QStringRK8QVariant(
    QDesignerIntegrationInterface *self,
    QDesignerFormWindowInterface *formWindow,
    const QString *name,
    const QVariant *value) {
  self->propertyChanged(formWindow, *name, *value);
}

//  void QDesignerIntegrationInterface::objectNameChanged(QDesignerFormWindow
//      Interface *formWindow, QObject *object, const QString &newName, const
//      QString &oldName)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface17objectNameChangedEP28QDesignerFormWindowInterfaceP7QObjectRK7QStringS6_(
    QDesignerIntegrationInterface *self,
    QDesignerFormWindowInterface *formWindow,
    QObject *object,
    const QString *newName,
    const QString *oldName) {
  self->objectNameChanged(formWindow, object, *newName, *oldName);
}

//  void QDesignerIntegrationInterface::helpRequested(const QString &manual,
//      const QString &document)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface13helpRequestedERK7QStringS2_(
    QDesignerIntegrationInterface *self,
    const QString *manual,
    const QString *document) {
  self->helpRequested(*manual, *document);
}

//  void QDesignerIntegrationInterface::navigateToSlot(const QString
//      &objectName, const QString &signalSignature, const QStringList
//      &parameterNames)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface14navigateToSlotERK7QStringS2_RK5QListIS0_E(
    QDesignerIntegrationInterface *self,
    const QString *objectName,
    const QString *signalSignature,
    const QList<QString> *parameterNames) {
  self->navigateToSlot(*objectName, *signalSignature, *parameterNames);
}

//  void QDesignerIntegrationInterface::navigateToSlot(const QString
//      &slotSignature)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface14navigateToSlotERK7QString(
    QDesignerIntegrationInterface *self,
    const QString *slotSignature) {
  self->navigateToSlot(*slotSignature);
}

//  void QDesignerIntegrationInterface::setFeatures(Feature f)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface11setFeaturesE6QFlagsINS_11FeatureFlagEE(
    QDesignerIntegrationInterface *self,
    int f) {
  self->setFeatures(
      QFlags<QDesignerIntegrationInterface::FeatureFlag>::fromInt(f));
}

//  void QDesignerIntegrationInterface::updateProperty(const QString &name,
//      const QVariant &value, bool enableSubPropertyHandling)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface14updatePropertyERK7QStringRK8QVariantb(
    QDesignerIntegrationInterface *self,
    const QString *name,
    const QVariant *value,
    bool enableSubPropertyHandling) {
  self->updateProperty(*name, *value, enableSubPropertyHandling);
}

//  void QDesignerIntegrationInterface::updateProperty(const QString &name,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface14updatePropertyERK7QStringRK8QVariant(
    QDesignerIntegrationInterface *self,
    const QString *name,
    const QVariant *value) {
  self->updateProperty(*name, *value);
}

//  void QDesignerIntegrationInterface::resetProperty(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface13resetPropertyERK7QString(
    QDesignerIntegrationInterface *self,
    const QString *name) {
  self->resetProperty(*name);
}

//  void QDesignerIntegrationInterface::addDynamicProperty(const QString
//      &name, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface18addDynamicPropertyERK7QStringRK8QVariant(
    QDesignerIntegrationInterface *self,
    const QString *name,
    const QVariant *value) {
  self->addDynamicProperty(*name, *value);
}

//  void QDesignerIntegrationInterface::removeDynamicProperty(const QString
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface21removeDynamicPropertyERK7QString(
    QDesignerIntegrationInterface *self,
    const QString *name) {
  self->removeDynamicProperty(*name);
}

//  void QDesignerIntegrationInterface::updateActiveFormWindow(QDesignerFormW
//      indowInterface *formWindow)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface22updateActiveFormWindowEP28QDesignerFormWindowInterface(
    QDesignerIntegrationInterface *self,
    QDesignerFormWindowInterface *formWindow) {
  self->updateActiveFormWindow(formWindow);
}

//  void QDesignerIntegrationInterface::setupFormWindow(QDesignerFormWindowIn
//      terface *formWindow)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface15setupFormWindowEP28QDesignerFormWindowInterface(
    QDesignerIntegrationInterface *self,
    QDesignerFormWindowInterface *formWindow) {
  self->setupFormWindow(formWindow);
}

//  void QDesignerIntegrationInterface::updateSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface15updateSelectionEv(
    QDesignerIntegrationInterface *self) {
  self->updateSelection();
}

//  void QDesignerIntegrationInterface::updateCustomWidgetPlugins()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerIntegrationInterface25updateCustomWidgetPluginsEv(
    QDesignerIntegrationInterface *self) {
  self->updateCustomWidgetPlugins();
}

//  a Python function taken by a CuteQDesignerIntegrationInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerIntegrationInterface(
    QDesignerIntegrationInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerIntegrationInterface *>(self)->take(key, call);
}
