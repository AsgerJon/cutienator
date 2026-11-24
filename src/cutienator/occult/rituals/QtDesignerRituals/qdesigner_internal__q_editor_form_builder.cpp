//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qsimpleresource_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qsimpleresource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A qdesigner_internal::QEditorFormBuilder that Python can take functions over in. Every qdesigner_internal::QEditorFormBuilder
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*Cuteqdesigner_internal_QEditorFormBuilderCall0)(const void *, QIODevice *, const qdesigner_internal::FormBuilderClipboard *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall1)(const void *, const qdesigner_internal::FormBuilderClipboard *, int *);
typedef const qdesigner_internal::FormBuilderClipboard * (*Cuteqdesigner_internal_QEditorFormBuilderCall2)(const void *, DomUI *, QWidget *, QObject *, int *);
typedef const qdesigner_internal::FormBuilderClipboard * (*Cuteqdesigner_internal_QEditorFormBuilderCall3)(const void *, QIODevice *, QWidget *, QObject *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall4)(const void *, QIODevice *, QWidget *, int *);
typedef void (*Cuteqdesigner_internal_QEditorFormBuilderCall5)(const void *, QIODevice *, QWidget *, int *);
typedef void (*Cuteqdesigner_internal_QEditorFormBuilderCall6)(const void *, DomWidget *, QWidget *, QWidget *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall7)(const void *, DomUI *, QWidget *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall8)(const void *, DomWidget *, QWidget *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall9)(const void *, DomLayout *, QLayout *, QWidget *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall10)(const void *, DomLayoutItem *, QLayout *, QWidget *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall11)(const void *, DomAction *, QObject *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall12)(const void *, DomActionGroup *, QObject *, int *);
typedef void (*Cuteqdesigner_internal_QEditorFormBuilderCall13)(const void *, QAction *, int *);
typedef void (*Cuteqdesigner_internal_QEditorFormBuilderCall14)(const void *, QWidget *, DomTabStops *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall15)(const void *, const QString *, QWidget *, const QString *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall16)(const void *, const QString *, QObject *, const QString *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall17)(const void *, QObject *, const QString *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall18)(const void *, QObject *, const QString *, int *);
typedef void (*Cuteqdesigner_internal_QEditorFormBuilderCall19)(const void *, DomCustomWidgets *, int *);
typedef void (*Cuteqdesigner_internal_QEditorFormBuilderCall20)(const void *, DomConnections *, QWidget *, int *);
typedef void (*Cuteqdesigner_internal_QEditorFormBuilderCall21)(const void *, DomResources *, int *);
typedef bool (*Cuteqdesigner_internal_QEditorFormBuilderCall22)(const void *, DomLayoutItem *, QLayoutItem *, QLayout *, int *);
typedef bool (*Cuteqdesigner_internal_QEditorFormBuilderCall23)(const void *, DomWidget *, QWidget *, QWidget *, int *);
typedef void (*Cuteqdesigner_internal_QEditorFormBuilderCall24)(const void *, QWidget *, DomWidget *, DomWidget *, int *);
typedef void (*Cuteqdesigner_internal_QEditorFormBuilderCall25)(const void *, DomUI *, QWidget *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall26)(const void *, QAction *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall27)(const void *, QWidget *, DomWidget *, bool, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall28)(const void *, QLayout *, DomLayout *, DomWidget *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall29)(const void *, QLayoutItem *, DomLayout *, DomWidget *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall30)(const void *, QSpacerItem *, DomLayout *, DomWidget *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall31)(const void *, QAction *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall32)(const void *, QActionGroup *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall33)(const void *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall34)(const void *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall35)(const void *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall36)(const void *, int *);
typedef bool (*Cuteqdesigner_internal_QEditorFormBuilderCall37)(const void *, QObject *, const QString *, int *);
typedef void * (*Cuteqdesigner_internal_QEditorFormBuilderCall38)(const void *, QObject *, const QString *, const QVariant *, int *);
class Cuteqdesigner_internal_QEditorFormBuilder : public qdesigner_internal::QEditorFormBuilder {
public:
  using qdesigner_internal::QEditorFormBuilder::QEditorFormBuilder;
  void *taken[39] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18qdesigner_internal18QEditorFormBuilder4copyEP9QIODeviceRKNS_20FormBuilderClipboardE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal18QEditorFormBuilder4copyERKNS_20FormBuilderClipboardE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal18QEditorFormBuilder5pasteEP5DomUIP7QWidgetP7QObject")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal18QEditorFormBuilder5pasteEP9QIODeviceP7QWidgetP7QObject")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder4loadEP9QIODeviceP7QWidget")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder4saveEP9QIODeviceP7QWidget")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder13loadExtraInfoEP9DomWidgetP7QWidgetS3_")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder6createEP5DomUIP7QWidget")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder6createEP9DomWidgetP7QWidget")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder6createEP9DomLayoutP7QLayoutP7QWidget")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder6createEP13DomLayoutItemP7QLayoutP7QWidget")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder6createEP9DomActionP7QObject")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder6createEP14DomActionGroupP7QObject")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder13addMenuActionEP7QAction")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder13applyTabStopsEP7QWidgetP11DomTabStops")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder12createWidgetERK7QStringP7QWidgetS2_")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder12createLayoutERK7QStringP7QObjectS2_")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder12createActionEP7QObjectRK7QString")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder17createActionGroupEP7QObjectRK7QString")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder19createCustomWidgetsEP16DomCustomWidgets")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder17createConnectionsEP14DomConnectionsP7QWidget")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder15createResourcesEP12DomResources")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder7addItemEP13DomLayoutItemP11QLayoutItemP7QLayout")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder7addItemEP9DomWidgetP7QWidgetS3_")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder13saveExtraInfoEP7QWidgetP9DomWidgetS3_")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder7saveDomEP5DomUIP7QWidget")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder18createActionRefDomEP7QAction")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder9createDomEP7QWidgetP9DomWidgetb")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder9createDomEP7QLayoutP9DomLayoutP9DomWidget")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder9createDomEP11QLayoutItemP9DomLayoutP9DomWidget")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder9createDomEP11QSpacerItemP9DomLayoutP9DomWidget")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder9createDomEP7QAction")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder9createDomEP12QActionGroup")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder15saveConnectionsEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder17saveCustomWidgetsEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder12saveTabStopsEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder13saveResourcesEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAbstractFormBuilder13checkPropertyEP7QObjectRK7QString")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder14createPropertyEP7QObjectRK7QStringRK8QVariant")) {
      taken[38] = call;
      return true;
    }
    return false;
  }

  //  bool qdesigner_internal::QEditorFormBuilder::copy(QIODevice *dev,
  //      const FormBuilderClipboard &selection)
  bool copy(
      QIODevice *dev,
      const qdesigner_internal::FormBuilderClipboard &selection) override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall0 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall0>(taken[0]);
      bool given = call(this, dev, &selection, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  DomUI *qdesigner_internal::QEditorFormBuilder::copy(const
  //      FormBuilderClipboard &selection)
  DomUI *copy(
      const qdesigner_internal::FormBuilderClipboard &selection) override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall1 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall1>(taken[1]);
      void * given = call(this, &selection, &handled);
      if (handled) return static_cast<DomUI *>(given);
    }
    return {};
  }

  //  FormBuilderClipboard
  //      qdesigner_internal::QEditorFormBuilder::paste(DomUI *ui, QWidget
  //      *widgetParent, QObject *actionParent)
  qdesigner_internal::FormBuilderClipboard paste(
      DomUI *ui,
      QWidget *widgetParent,
      QObject *actionParent) override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall2 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall2>(taken[2]);
      const qdesigner_internal::FormBuilderClipboard * given = call(this, ui, widgetParent, actionParent, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  FormBuilderClipboard
  //      qdesigner_internal::QEditorFormBuilder::paste(QIODevice *dev,
  //      QWidget *widgetParent, QObject *actionParent)
  qdesigner_internal::FormBuilderClipboard paste(
      QIODevice *dev,
      QWidget *widgetParent,
      QObject *actionParent) override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall3 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall3>(taken[3]);
      const qdesigner_internal::FormBuilderClipboard * given = call(this, dev, widgetParent, actionParent, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QWidget *QAbstractFormBuilder::load(QIODevice *dev, QWidget
  //      *parentWidget)
  QWidget *load(QIODevice *dev, QWidget *parentWidget) override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall4 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall4>(taken[4]);
      void * given = call(this, dev, parentWidget, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QAbstractFormBuilder::load(dev, parentWidget);
  }

  //  void QAbstractFormBuilder::save(QIODevice *dev, QWidget *widget)
  void save(QIODevice *dev, QWidget *widget) override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall5 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall5>(taken[5]);
      call(this, dev, widget, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::save(dev, widget);
  }

  //  void QAbstractFormBuilder::loadExtraInfo(DomWidget *ui_widget,
  //      QWidget *widget, QWidget *parentWidget)
  void loadExtraInfo(
      DomWidget *ui_widget,
      QWidget *widget,
      QWidget *parentWidget) override {
    if (taken[6]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall6 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall6>(taken[6]);
      call(this, ui_widget, widget, parentWidget, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::loadExtraInfo(ui_widget, widget, parentWidget);
  }

  //  QWidget *QAbstractFormBuilder::create(DomUI *ui, QWidget
  //      *parentWidget)
  QWidget *create(DomUI *ui, QWidget *parentWidget) override {
    if (taken[7]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall7 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall7>(taken[7]);
      void * given = call(this, ui, parentWidget, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QAbstractFormBuilder::create(ui, parentWidget);
  }

  //  QWidget *QAbstractFormBuilder::create(DomWidget *ui_widget, QWidget
  //      *parentWidget)
  QWidget *create(DomWidget *ui_widget, QWidget *parentWidget) override {
    if (taken[8]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall8 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall8>(taken[8]);
      void * given = call(this, ui_widget, parentWidget, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QAbstractFormBuilder::create(ui_widget, parentWidget);
  }

  //  QLayout *QAbstractFormBuilder::create(DomLayout *ui_layout, QLayout
  //      *layout, QWidget *parentWidget)
  QLayout *create(
      DomLayout *ui_layout,
      QLayout *layout,
      QWidget *parentWidget) override {
    if (taken[9]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall9 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall9>(taken[9]);
      void * given = call(this, ui_layout, layout, parentWidget, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return QAbstractFormBuilder::create(ui_layout, layout, parentWidget);
  }

  //  QLayoutItem *QAbstractFormBuilder::create(DomLayoutItem
  //      *ui_layoutItem, QLayout *layout, QWidget *parentWidget)
  QLayoutItem *create(
      DomLayoutItem *ui_layoutItem,
      QLayout *layout,
      QWidget *parentWidget) override {
    if (taken[10]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall10 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall10>(taken[10]);
      void * given = call(this, ui_layoutItem, layout, parentWidget, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QAbstractFormBuilder::create(ui_layoutItem, layout, parentWidget);
  }

  //  QAction *QAbstractFormBuilder::create(DomAction *ui_action, QObject
  //      *parent)
  QAction *create(DomAction *ui_action, QObject *parent) override {
    if (taken[11]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall11 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall11>(taken[11]);
      void * given = call(this, ui_action, parent, &handled);
      if (handled) return static_cast<QAction *>(given);
    }
    return QAbstractFormBuilder::create(ui_action, parent);
  }

  //  QActionGroup *QAbstractFormBuilder::create(DomActionGroup
  //      *ui_action_group, QObject *parent)
  QActionGroup *create(
      DomActionGroup *ui_action_group,
      QObject *parent) override {
    if (taken[12]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall12 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall12>(taken[12]);
      void * given = call(this, ui_action_group, parent, &handled);
      if (handled) return static_cast<QActionGroup *>(given);
    }
    return QAbstractFormBuilder::create(ui_action_group, parent);
  }

  //  void QAbstractFormBuilder::addMenuAction(QAction *action)
  void addMenuAction(QAction *action) override {
    if (taken[13]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall13 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall13>(taken[13]);
      call(this, action, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::addMenuAction(action);
  }

  //  void QAbstractFormBuilder::applyTabStops(QWidget *widget, DomTabStops
  //      *tabStops)
  void applyTabStops(QWidget *widget, DomTabStops *tabStops) override {
    if (taken[14]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall14 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall14>(taken[14]);
      call(this, widget, tabStops, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::applyTabStops(widget, tabStops);
  }

  //  QWidget *QAbstractFormBuilder::createWidget(const QString
  //      &widgetName, QWidget *parentWidget, const QString &name)
  QWidget *createWidget(
      const QString &widgetName,
      QWidget *parentWidget,
      const QString &name) override {
    if (taken[15]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall15 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall15>(taken[15]);
      void * given = call(this, &widgetName, parentWidget, &name, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QAbstractFormBuilder::createWidget(widgetName, parentWidget, name);
  }

  //  QLayout *QAbstractFormBuilder::createLayout(const QString
  //      &layoutName, QObject *parent, const QString &name)
  QLayout *createLayout(
      const QString &layoutName,
      QObject *parent,
      const QString &name) override {
    if (taken[16]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall16 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall16>(taken[16]);
      void * given = call(this, &layoutName, parent, &name, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return QAbstractFormBuilder::createLayout(layoutName, parent, name);
  }

  //  QAction *QAbstractFormBuilder::createAction(QObject *parent, const
  //      QString &name)
  QAction *createAction(QObject *parent, const QString &name) override {
    if (taken[17]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall17 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall17>(taken[17]);
      void * given = call(this, parent, &name, &handled);
      if (handled) return static_cast<QAction *>(given);
    }
    return QAbstractFormBuilder::createAction(parent, name);
  }

  //  QActionGroup *QAbstractFormBuilder::createActionGroup(QObject
  //      *parent, const QString &name)
  QActionGroup *createActionGroup(
      QObject *parent,
      const QString &name) override {
    if (taken[18]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall18 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall18>(taken[18]);
      void * given = call(this, parent, &name, &handled);
      if (handled) return static_cast<QActionGroup *>(given);
    }
    return QAbstractFormBuilder::createActionGroup(parent, name);
  }

  //  void QAbstractFormBuilder::createCustomWidgets(DomCustomWidgets *a0)
  void createCustomWidgets(DomCustomWidgets *a0) override {
    if (taken[19]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall19 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::createCustomWidgets(a0);
  }

  //  void QAbstractFormBuilder::createConnections(DomConnections *a0,
  //      QWidget *a1)
  void createConnections(DomConnections *a0, QWidget *a1) override {
    if (taken[20]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall20 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall20>(taken[20]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::createConnections(a0, a1);
  }

  //  void QAbstractFormBuilder::createResources(DomResources *a0)
  void createResources(DomResources *a0) override {
    if (taken[21]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall21 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::createResources(a0);
  }

  //  bool QAbstractFormBuilder::addItem(DomLayoutItem *ui_item,
  //      QLayoutItem *item, QLayout *layout)
  bool addItem(
      DomLayoutItem *ui_item,
      QLayoutItem *item,
      QLayout *layout) override {
    if (taken[22]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall22 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall22>(taken[22]);
      bool given = call(this, ui_item, item, layout, &handled);
      if (handled) return given;
    }
    return QAbstractFormBuilder::addItem(ui_item, item, layout);
  }

  //  bool QAbstractFormBuilder::addItem(DomWidget *ui_widget, QWidget
  //      *widget, QWidget *parentWidget)
  bool addItem(
      DomWidget *ui_widget,
      QWidget *widget,
      QWidget *parentWidget) override {
    if (taken[23]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall23 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall23>(taken[23]);
      bool given = call(this, ui_widget, widget, parentWidget, &handled);
      if (handled) return given;
    }
    return QAbstractFormBuilder::addItem(ui_widget, widget, parentWidget);
  }

  //  void QAbstractFormBuilder::saveExtraInfo(QWidget *widget, DomWidget
  //      *ui_widget, DomWidget *ui_parentWidget)
  void saveExtraInfo(
      QWidget *widget,
      DomWidget *ui_widget,
      DomWidget *ui_parentWidget) override {
    if (taken[24]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall24 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall24>(taken[24]);
      call(this, widget, ui_widget, ui_parentWidget, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::saveExtraInfo(widget, ui_widget, ui_parentWidget);
  }

  //  void QAbstractFormBuilder::saveDom(DomUI *ui, QWidget *widget)
  void saveDom(DomUI *ui, QWidget *widget) override {
    if (taken[25]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall25 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall25>(taken[25]);
      call(this, ui, widget, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::saveDom(ui, widget);
  }

  //  DomActionRef *QAbstractFormBuilder::createActionRefDom(QAction
  //      *action)
  DomActionRef *createActionRefDom(QAction *action) override {
    if (taken[26]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall26 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall26>(taken[26]);
      void * given = call(this, action, &handled);
      if (handled) return static_cast<DomActionRef *>(given);
    }
    return QAbstractFormBuilder::createActionRefDom(action);
  }

  //  DomWidget *QAbstractFormBuilder::createDom(QWidget *widget, DomWidget
  //      *ui_parentWidget, bool recursive)
  DomWidget *createDom(
      QWidget *widget,
      DomWidget *ui_parentWidget,
      bool recursive) override {
    if (taken[27]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall27 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall27>(taken[27]);
      void * given = call(this, widget, ui_parentWidget, recursive, &handled);
      if (handled) return static_cast<DomWidget *>(given);
    }
    return QAbstractFormBuilder::createDom(widget, ui_parentWidget, recursive);
  }

  //  DomLayout *QAbstractFormBuilder::createDom(QLayout *layout, DomLayout
  //      *ui_layout, DomWidget *ui_parentWidget)
  DomLayout *createDom(
      QLayout *layout,
      DomLayout *ui_layout,
      DomWidget *ui_parentWidget) override {
    if (taken[28]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall28 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall28>(taken[28]);
      void * given = call(this, layout, ui_layout, ui_parentWidget, &handled);
      if (handled) return static_cast<DomLayout *>(given);
    }
    return QAbstractFormBuilder::createDom(layout, ui_layout, ui_parentWidget);
  }

  //  DomLayoutItem *QAbstractFormBuilder::createDom(QLayoutItem *item,
  //      DomLayout *ui_parentLayout, DomWidget *ui_parentWidget)
  DomLayoutItem *createDom(
      QLayoutItem *item,
      DomLayout *ui_parentLayout,
      DomWidget *ui_parentWidget) override {
    if (taken[29]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall29 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall29>(taken[29]);
      void * given = call(this, item, ui_parentLayout, ui_parentWidget, &handled);
      if (handled) return static_cast<DomLayoutItem *>(given);
    }
    return QAbstractFormBuilder::createDom(item, ui_parentLayout, ui_parentWidget);
  }

  //  DomSpacer *QAbstractFormBuilder::createDom(QSpacerItem *spacer,
  //      DomLayout *ui_parentLayout, DomWidget *ui_parentWidget)
  DomSpacer *createDom(
      QSpacerItem *spacer,
      DomLayout *ui_parentLayout,
      DomWidget *ui_parentWidget) override {
    if (taken[30]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall30 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall30>(taken[30]);
      void * given = call(this, spacer, ui_parentLayout, ui_parentWidget, &handled);
      if (handled) return static_cast<DomSpacer *>(given);
    }
    return QAbstractFormBuilder::createDom(spacer, ui_parentLayout, ui_parentWidget);
  }

  //  DomAction *QAbstractFormBuilder::createDom(QAction *action)
  DomAction *createDom(QAction *action) override {
    if (taken[31]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall31 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall31>(taken[31]);
      void * given = call(this, action, &handled);
      if (handled) return static_cast<DomAction *>(given);
    }
    return QAbstractFormBuilder::createDom(action);
  }

  //  DomActionGroup *QAbstractFormBuilder::createDom(QActionGroup
  //      *actionGroup)
  DomActionGroup *createDom(QActionGroup *actionGroup) override {
    if (taken[32]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall32 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall32>(taken[32]);
      void * given = call(this, actionGroup, &handled);
      if (handled) return static_cast<DomActionGroup *>(given);
    }
    return QAbstractFormBuilder::createDom(actionGroup);
  }

  //  DomConnections *QAbstractFormBuilder::saveConnections()
  DomConnections *saveConnections() override {
    if (taken[33]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall33 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall33>(taken[33]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DomConnections *>(given);
    }
    return QAbstractFormBuilder::saveConnections();
  }

  //  DomCustomWidgets *QAbstractFormBuilder::saveCustomWidgets()
  DomCustomWidgets *saveCustomWidgets() override {
    if (taken[34]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall34 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall34>(taken[34]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DomCustomWidgets *>(given);
    }
    return QAbstractFormBuilder::saveCustomWidgets();
  }

  //  DomTabStops *QAbstractFormBuilder::saveTabStops()
  DomTabStops *saveTabStops() override {
    if (taken[35]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall35 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall35>(taken[35]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DomTabStops *>(given);
    }
    return QAbstractFormBuilder::saveTabStops();
  }

  //  DomResources *QAbstractFormBuilder::saveResources()
  DomResources *saveResources() override {
    if (taken[36]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall36 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DomResources *>(given);
    }
    return QAbstractFormBuilder::saveResources();
  }

  //  bool QAbstractFormBuilder::checkProperty(QObject *obj, const QString
  //      &prop) const
  bool checkProperty(QObject *obj, const QString &prop) const override {
    if (taken[37]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall37 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall37>(taken[37]);
      bool given = call(this, obj, &prop, &handled);
      if (handled) return given;
    }
    return QAbstractFormBuilder::checkProperty(obj, prop);
  }

  //  DomProperty *QAbstractFormBuilder::createProperty(QObject *object,
  //      const QString &propertyName, const QVariant &value)
  DomProperty *createProperty(
      QObject *object,
      const QString &propertyName,
      const QVariant &value) override {
    if (taken[38]) {
      int handled = 0;
      Cuteqdesigner_internal_QEditorFormBuilderCall38 call = reinterpret_cast<Cuteqdesigner_internal_QEditorFormBuilderCall38>(taken[38]);
      void * given = call(this, object, &propertyName, &value, &handled);
      if (handled) return static_cast<DomProperty *>(given);
    }
    return QAbstractFormBuilder::createProperty(object, propertyName, value);
  }
};

//  bool qdesigner_internal::QEditorFormBuilder::copy(QIODevice *dev, const
//      FormBuilderClipboard &selection)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal18QEditorFormBuilder4copyEP9QIODeviceRKNS_20FormBuilderClipboardE(
    qdesigner_internal::QEditorFormBuilder *self,
    QIODevice *dev,
    const qdesigner_internal::FormBuilderClipboard *selection) {
  return self->copy(dev, *selection);
}

//  DomUI *qdesigner_internal::QEditorFormBuilder::copy(const
//      FormBuilderClipboard &selection)
extern "C" Q_DECL_EXPORT
DomUI *ritual_ZN18qdesigner_internal18QEditorFormBuilder4copyERKNS_20FormBuilderClipboardE(
    qdesigner_internal::QEditorFormBuilder *self,
    const qdesigner_internal::FormBuilderClipboard *selection) {
  return self->copy(*selection);
}

//  FormBuilderClipboard qdesigner_internal::QEditorFormBuilder::paste(DomUI
//      *ui, QWidget *widgetParent, QObject *actionParent)
extern "C" Q_DECL_EXPORT
qdesigner_internal::FormBuilderClipboard *ritual_ZN18qdesigner_internal18QEditorFormBuilder5pasteEP5DomUIP7QWidgetP7QObject(
    qdesigner_internal::QEditorFormBuilder *self,
    DomUI *ui,
    QWidget *widgetParent,
    QObject *actionParent) {
  return new qdesigner_internal::FormBuilderClipboard(
      self->paste(
          ui,
          widgetParent,
          actionParent));
}

//  FormBuilderClipboard
//      qdesigner_internal::QEditorFormBuilder::paste(QIODevice *dev, QWidget
//      *widgetParent, QObject *actionParent)
extern "C" Q_DECL_EXPORT
qdesigner_internal::FormBuilderClipboard *ritual_ZN18qdesigner_internal18QEditorFormBuilder5pasteEP9QIODeviceP7QWidgetP7QObject(
    qdesigner_internal::QEditorFormBuilder *self,
    QIODevice *dev,
    QWidget *widgetParent,
    QObject *actionParent) {
  return new qdesigner_internal::FormBuilderClipboard(
      self->paste(
          dev,
          widgetParent,
          actionParent));
}

//  a Python function taken by a Cuteqdesigner_internal_QEditorFormBuilder,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_QEditorFormBuilder(
    qdesigner_internal::QEditorFormBuilder *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_QEditorFormBuilder *>(self)->take(key, call);
}
