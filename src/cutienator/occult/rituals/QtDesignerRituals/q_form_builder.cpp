//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/formbuilder.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/formbuilder.h>
#include <QtCore/qstring.h>
#include <QtUiPlugin/customwidget.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QFormBuilder may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQFormBuilder : QFormBuilder {
  using QFormBuilder::create;
  using QFormBuilder::createWidget;
  using QFormBuilder::createLayout;
  using QFormBuilder::createConnections;
  using QFormBuilder::addItem;
  using QFormBuilder::updateCustomWidgets;
};

//  A QFormBuilder that Python can take functions over in. Every QFormBuilder
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQFormBuilderCall0)(const void *, DomUI *, QWidget *, int *);
typedef void * (*CuteQFormBuilderCall1)(const void *, DomWidget *, QWidget *, int *);
typedef void * (*CuteQFormBuilderCall2)(const void *, DomLayout *, QLayout *, QWidget *, int *);
typedef void * (*CuteQFormBuilderCall3)(const void *, DomLayoutItem *, QLayout *, QWidget *, int *);
typedef void * (*CuteQFormBuilderCall4)(const void *, DomAction *, QObject *, int *);
typedef void * (*CuteQFormBuilderCall5)(const void *, DomActionGroup *, QObject *, int *);
typedef void * (*CuteQFormBuilderCall6)(const void *, const QString *, QWidget *, const QString *, int *);
typedef void * (*CuteQFormBuilderCall7)(const void *, const QString *, QObject *, const QString *, int *);
typedef void (*CuteQFormBuilderCall8)(const void *, DomConnections *, QWidget *, int *);
typedef bool (*CuteQFormBuilderCall9)(const void *, DomLayoutItem *, QLayoutItem *, QLayout *, int *);
typedef bool (*CuteQFormBuilderCall10)(const void *, DomWidget *, QWidget *, QWidget *, int *);
typedef void (*CuteQFormBuilderCall11)(const void *, int *);
typedef void * (*CuteQFormBuilderCall12)(const void *, QIODevice *, QWidget *, int *);
typedef void (*CuteQFormBuilderCall13)(const void *, QIODevice *, QWidget *, int *);
typedef void (*CuteQFormBuilderCall14)(const void *, DomWidget *, QWidget *, QWidget *, int *);
typedef void (*CuteQFormBuilderCall15)(const void *, QAction *, int *);
typedef void (*CuteQFormBuilderCall16)(const void *, QWidget *, DomTabStops *, int *);
typedef void * (*CuteQFormBuilderCall17)(const void *, QObject *, const QString *, int *);
typedef void * (*CuteQFormBuilderCall18)(const void *, QObject *, const QString *, int *);
typedef void (*CuteQFormBuilderCall19)(const void *, DomCustomWidgets *, int *);
typedef void (*CuteQFormBuilderCall20)(const void *, DomResources *, int *);
typedef void (*CuteQFormBuilderCall21)(const void *, QWidget *, DomWidget *, DomWidget *, int *);
typedef void (*CuteQFormBuilderCall22)(const void *, DomUI *, QWidget *, int *);
typedef void * (*CuteQFormBuilderCall23)(const void *, QAction *, int *);
typedef void * (*CuteQFormBuilderCall24)(const void *, QWidget *, DomWidget *, bool, int *);
typedef void * (*CuteQFormBuilderCall25)(const void *, QLayout *, DomLayout *, DomWidget *, int *);
typedef void * (*CuteQFormBuilderCall26)(const void *, QLayoutItem *, DomLayout *, DomWidget *, int *);
typedef void * (*CuteQFormBuilderCall27)(const void *, QSpacerItem *, DomLayout *, DomWidget *, int *);
typedef void * (*CuteQFormBuilderCall28)(const void *, QAction *, int *);
typedef void * (*CuteQFormBuilderCall29)(const void *, QActionGroup *, int *);
typedef void * (*CuteQFormBuilderCall30)(const void *, int *);
typedef void * (*CuteQFormBuilderCall31)(const void *, int *);
typedef void * (*CuteQFormBuilderCall32)(const void *, int *);
typedef void * (*CuteQFormBuilderCall33)(const void *, int *);
typedef bool (*CuteQFormBuilderCall34)(const void *, QObject *, const QString *, int *);
typedef void * (*CuteQFormBuilderCall35)(const void *, QObject *, const QString *, const QVariant *, int *);
class CuteQFormBuilder : public QFormBuilder {
public:
  using QFormBuilder::QFormBuilder;
  void *taken[36] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder6createEP5DomUIP7QWidget")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder6createEP9DomWidgetP7QWidget")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder6createEP9DomLayoutP7QLayoutP7QWidget")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder6createEP13DomLayoutItemP7QLayoutP7QWidget")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder6createEP9DomActionP7QObject")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder6createEP14DomActionGroupP7QObject")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder12createWidgetERK7QStringP7QWidgetS2_")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder12createLayoutERK7QStringP7QObjectS2_")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder17createConnectionsEP14DomConnectionsP7QWidget")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder7addItemEP13DomLayoutItemP11QLayoutItemP7QLayout")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder7addItemEP9DomWidgetP7QWidgetS3_")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QFormBuilder19updateCustomWidgetsEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder4loadEP9QIODeviceP7QWidget")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder4saveEP9QIODeviceP7QWidget")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder13loadExtraInfoEP9DomWidgetP7QWidgetS3_")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder13addMenuActionEP7QAction")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder13applyTabStopsEP7QWidgetP11DomTabStops")) {
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
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder15createResourcesEP12DomResources")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder13saveExtraInfoEP7QWidgetP9DomWidgetS3_")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder7saveDomEP5DomUIP7QWidget")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder18createActionRefDomEP7QAction")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder9createDomEP7QWidgetP9DomWidgetb")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder9createDomEP7QLayoutP9DomLayoutP9DomWidget")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder9createDomEP11QLayoutItemP9DomLayoutP9DomWidget")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder9createDomEP11QSpacerItemP9DomLayoutP9DomWidget")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder9createDomEP7QAction")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder9createDomEP12QActionGroup")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder15saveConnectionsEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder17saveCustomWidgetsEv")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder12saveTabStopsEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder13saveResourcesEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAbstractFormBuilder13checkPropertyEP7QObjectRK7QString")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder14createPropertyEP7QObjectRK7QStringRK8QVariant")) {
      taken[35] = call;
      return true;
    }
    return false;
  }

  //  QWidget *QFormBuilder::create(DomUI *ui, QWidget *parentWidget)
  QWidget *create(DomUI *ui, QWidget *parentWidget) override {
    if (taken[0]) {
      int handled = 0;
      CuteQFormBuilderCall0 call = reinterpret_cast<CuteQFormBuilderCall0>(taken[0]);
      void * given = call(this, ui, parentWidget, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QFormBuilder::create(ui, parentWidget);
  }

  //  QWidget *QFormBuilder::create(DomWidget *ui_widget, QWidget
  //      *parentWidget)
  QWidget *create(DomWidget *ui_widget, QWidget *parentWidget) override {
    if (taken[1]) {
      int handled = 0;
      CuteQFormBuilderCall1 call = reinterpret_cast<CuteQFormBuilderCall1>(taken[1]);
      void * given = call(this, ui_widget, parentWidget, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QFormBuilder::create(ui_widget, parentWidget);
  }

  //  QLayout *QFormBuilder::create(DomLayout *ui_layout, QLayout *layout,
  //      QWidget *parentWidget)
  QLayout *create(
      DomLayout *ui_layout,
      QLayout *layout,
      QWidget *parentWidget) override {
    if (taken[2]) {
      int handled = 0;
      CuteQFormBuilderCall2 call = reinterpret_cast<CuteQFormBuilderCall2>(taken[2]);
      void * given = call(this, ui_layout, layout, parentWidget, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return QFormBuilder::create(ui_layout, layout, parentWidget);
  }

  //  QLayoutItem *QFormBuilder::create(DomLayoutItem *ui_layoutItem,
  //      QLayout *layout, QWidget *parentWidget)
  QLayoutItem *create(
      DomLayoutItem *ui_layoutItem,
      QLayout *layout,
      QWidget *parentWidget) override {
    if (taken[3]) {
      int handled = 0;
      CuteQFormBuilderCall3 call = reinterpret_cast<CuteQFormBuilderCall3>(taken[3]);
      void * given = call(this, ui_layoutItem, layout, parentWidget, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QFormBuilder::create(ui_layoutItem, layout, parentWidget);
  }

  //  QAction *QFormBuilder::create(DomAction *ui_action, QObject *parent)
  QAction *create(DomAction *ui_action, QObject *parent) override {
    if (taken[4]) {
      int handled = 0;
      CuteQFormBuilderCall4 call = reinterpret_cast<CuteQFormBuilderCall4>(taken[4]);
      void * given = call(this, ui_action, parent, &handled);
      if (handled) return static_cast<QAction *>(given);
    }
    return QFormBuilder::create(ui_action, parent);
  }

  //  QActionGroup *QFormBuilder::create(DomActionGroup *ui_action_group,
  //      QObject *parent)
  QActionGroup *create(
      DomActionGroup *ui_action_group,
      QObject *parent) override {
    if (taken[5]) {
      int handled = 0;
      CuteQFormBuilderCall5 call = reinterpret_cast<CuteQFormBuilderCall5>(taken[5]);
      void * given = call(this, ui_action_group, parent, &handled);
      if (handled) return static_cast<QActionGroup *>(given);
    }
    return QFormBuilder::create(ui_action_group, parent);
  }

  //  QWidget *QFormBuilder::createWidget(const QString &widgetName,
  //      QWidget *parentWidget, const QString &name)
  QWidget *createWidget(
      const QString &widgetName,
      QWidget *parentWidget,
      const QString &name) override {
    if (taken[6]) {
      int handled = 0;
      CuteQFormBuilderCall6 call = reinterpret_cast<CuteQFormBuilderCall6>(taken[6]);
      void * given = call(this, &widgetName, parentWidget, &name, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QFormBuilder::createWidget(widgetName, parentWidget, name);
  }

  //  QLayout *QFormBuilder::createLayout(const QString &layoutName,
  //      QObject *parent, const QString &name)
  QLayout *createLayout(
      const QString &layoutName,
      QObject *parent,
      const QString &name) override {
    if (taken[7]) {
      int handled = 0;
      CuteQFormBuilderCall7 call = reinterpret_cast<CuteQFormBuilderCall7>(taken[7]);
      void * given = call(this, &layoutName, parent, &name, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return QFormBuilder::createLayout(layoutName, parent, name);
  }

  //  void QFormBuilder::createConnections(DomConnections *connections,
  //      QWidget *widget)
  void createConnections(
      DomConnections *connections,
      QWidget *widget) override {
    if (taken[8]) {
      int handled = 0;
      CuteQFormBuilderCall8 call = reinterpret_cast<CuteQFormBuilderCall8>(taken[8]);
      call(this, connections, widget, &handled);
      if (handled) return;
    }
    QFormBuilder::createConnections(connections, widget);
  }

  //  bool QFormBuilder::addItem(DomLayoutItem *ui_item, QLayoutItem *item,
  //      QLayout *layout)
  bool addItem(
      DomLayoutItem *ui_item,
      QLayoutItem *item,
      QLayout *layout) override {
    if (taken[9]) {
      int handled = 0;
      CuteQFormBuilderCall9 call = reinterpret_cast<CuteQFormBuilderCall9>(taken[9]);
      bool given = call(this, ui_item, item, layout, &handled);
      if (handled) return given;
    }
    return QFormBuilder::addItem(ui_item, item, layout);
  }

  //  bool QFormBuilder::addItem(DomWidget *ui_widget, QWidget *widget,
  //      QWidget *parentWidget)
  bool addItem(
      DomWidget *ui_widget,
      QWidget *widget,
      QWidget *parentWidget) override {
    if (taken[10]) {
      int handled = 0;
      CuteQFormBuilderCall10 call = reinterpret_cast<CuteQFormBuilderCall10>(taken[10]);
      bool given = call(this, ui_widget, widget, parentWidget, &handled);
      if (handled) return given;
    }
    return QFormBuilder::addItem(ui_widget, widget, parentWidget);
  }

  //  void QFormBuilder::updateCustomWidgets()
  void updateCustomWidgets() override {
    if (taken[11]) {
      int handled = 0;
      CuteQFormBuilderCall11 call = reinterpret_cast<CuteQFormBuilderCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QFormBuilder::updateCustomWidgets();
  }

  //  QWidget *QAbstractFormBuilder::load(QIODevice *dev, QWidget
  //      *parentWidget)
  QWidget *load(QIODevice *dev, QWidget *parentWidget) override {
    if (taken[12]) {
      int handled = 0;
      CuteQFormBuilderCall12 call = reinterpret_cast<CuteQFormBuilderCall12>(taken[12]);
      void * given = call(this, dev, parentWidget, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QAbstractFormBuilder::load(dev, parentWidget);
  }

  //  void QAbstractFormBuilder::save(QIODevice *dev, QWidget *widget)
  void save(QIODevice *dev, QWidget *widget) override {
    if (taken[13]) {
      int handled = 0;
      CuteQFormBuilderCall13 call = reinterpret_cast<CuteQFormBuilderCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteQFormBuilderCall14 call = reinterpret_cast<CuteQFormBuilderCall14>(taken[14]);
      call(this, ui_widget, widget, parentWidget, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::loadExtraInfo(ui_widget, widget, parentWidget);
  }

  //  void QAbstractFormBuilder::addMenuAction(QAction *action)
  void addMenuAction(QAction *action) override {
    if (taken[15]) {
      int handled = 0;
      CuteQFormBuilderCall15 call = reinterpret_cast<CuteQFormBuilderCall15>(taken[15]);
      call(this, action, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::addMenuAction(action);
  }

  //  void QAbstractFormBuilder::applyTabStops(QWidget *widget, DomTabStops
  //      *tabStops)
  void applyTabStops(QWidget *widget, DomTabStops *tabStops) override {
    if (taken[16]) {
      int handled = 0;
      CuteQFormBuilderCall16 call = reinterpret_cast<CuteQFormBuilderCall16>(taken[16]);
      call(this, widget, tabStops, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::applyTabStops(widget, tabStops);
  }

  //  QAction *QAbstractFormBuilder::createAction(QObject *parent, const
  //      QString &name)
  QAction *createAction(QObject *parent, const QString &name) override {
    if (taken[17]) {
      int handled = 0;
      CuteQFormBuilderCall17 call = reinterpret_cast<CuteQFormBuilderCall17>(taken[17]);
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
      CuteQFormBuilderCall18 call = reinterpret_cast<CuteQFormBuilderCall18>(taken[18]);
      void * given = call(this, parent, &name, &handled);
      if (handled) return static_cast<QActionGroup *>(given);
    }
    return QAbstractFormBuilder::createActionGroup(parent, name);
  }

  //  void QAbstractFormBuilder::createCustomWidgets(DomCustomWidgets *a0)
  void createCustomWidgets(DomCustomWidgets *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQFormBuilderCall19 call = reinterpret_cast<CuteQFormBuilderCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::createCustomWidgets(a0);
  }

  //  void QAbstractFormBuilder::createResources(DomResources *a0)
  void createResources(DomResources *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQFormBuilderCall20 call = reinterpret_cast<CuteQFormBuilderCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::createResources(a0);
  }

  //  void QAbstractFormBuilder::saveExtraInfo(QWidget *widget, DomWidget
  //      *ui_widget, DomWidget *ui_parentWidget)
  void saveExtraInfo(
      QWidget *widget,
      DomWidget *ui_widget,
      DomWidget *ui_parentWidget) override {
    if (taken[21]) {
      int handled = 0;
      CuteQFormBuilderCall21 call = reinterpret_cast<CuteQFormBuilderCall21>(taken[21]);
      call(this, widget, ui_widget, ui_parentWidget, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::saveExtraInfo(widget, ui_widget, ui_parentWidget);
  }

  //  void QAbstractFormBuilder::saveDom(DomUI *ui, QWidget *widget)
  void saveDom(DomUI *ui, QWidget *widget) override {
    if (taken[22]) {
      int handled = 0;
      CuteQFormBuilderCall22 call = reinterpret_cast<CuteQFormBuilderCall22>(taken[22]);
      call(this, ui, widget, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::saveDom(ui, widget);
  }

  //  DomActionRef *QAbstractFormBuilder::createActionRefDom(QAction
  //      *action)
  DomActionRef *createActionRefDom(QAction *action) override {
    if (taken[23]) {
      int handled = 0;
      CuteQFormBuilderCall23 call = reinterpret_cast<CuteQFormBuilderCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQFormBuilderCall24 call = reinterpret_cast<CuteQFormBuilderCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteQFormBuilderCall25 call = reinterpret_cast<CuteQFormBuilderCall25>(taken[25]);
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
    if (taken[26]) {
      int handled = 0;
      CuteQFormBuilderCall26 call = reinterpret_cast<CuteQFormBuilderCall26>(taken[26]);
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
    if (taken[27]) {
      int handled = 0;
      CuteQFormBuilderCall27 call = reinterpret_cast<CuteQFormBuilderCall27>(taken[27]);
      void * given = call(this, spacer, ui_parentLayout, ui_parentWidget, &handled);
      if (handled) return static_cast<DomSpacer *>(given);
    }
    return QAbstractFormBuilder::createDom(spacer, ui_parentLayout, ui_parentWidget);
  }

  //  DomAction *QAbstractFormBuilder::createDom(QAction *action)
  DomAction *createDom(QAction *action) override {
    if (taken[28]) {
      int handled = 0;
      CuteQFormBuilderCall28 call = reinterpret_cast<CuteQFormBuilderCall28>(taken[28]);
      void * given = call(this, action, &handled);
      if (handled) return static_cast<DomAction *>(given);
    }
    return QAbstractFormBuilder::createDom(action);
  }

  //  DomActionGroup *QAbstractFormBuilder::createDom(QActionGroup
  //      *actionGroup)
  DomActionGroup *createDom(QActionGroup *actionGroup) override {
    if (taken[29]) {
      int handled = 0;
      CuteQFormBuilderCall29 call = reinterpret_cast<CuteQFormBuilderCall29>(taken[29]);
      void * given = call(this, actionGroup, &handled);
      if (handled) return static_cast<DomActionGroup *>(given);
    }
    return QAbstractFormBuilder::createDom(actionGroup);
  }

  //  DomConnections *QAbstractFormBuilder::saveConnections()
  DomConnections *saveConnections() override {
    if (taken[30]) {
      int handled = 0;
      CuteQFormBuilderCall30 call = reinterpret_cast<CuteQFormBuilderCall30>(taken[30]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DomConnections *>(given);
    }
    return QAbstractFormBuilder::saveConnections();
  }

  //  DomCustomWidgets *QAbstractFormBuilder::saveCustomWidgets()
  DomCustomWidgets *saveCustomWidgets() override {
    if (taken[31]) {
      int handled = 0;
      CuteQFormBuilderCall31 call = reinterpret_cast<CuteQFormBuilderCall31>(taken[31]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DomCustomWidgets *>(given);
    }
    return QAbstractFormBuilder::saveCustomWidgets();
  }

  //  DomTabStops *QAbstractFormBuilder::saveTabStops()
  DomTabStops *saveTabStops() override {
    if (taken[32]) {
      int handled = 0;
      CuteQFormBuilderCall32 call = reinterpret_cast<CuteQFormBuilderCall32>(taken[32]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DomTabStops *>(given);
    }
    return QAbstractFormBuilder::saveTabStops();
  }

  //  DomResources *QAbstractFormBuilder::saveResources()
  DomResources *saveResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteQFormBuilderCall33 call = reinterpret_cast<CuteQFormBuilderCall33>(taken[33]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DomResources *>(given);
    }
    return QAbstractFormBuilder::saveResources();
  }

  //  bool QAbstractFormBuilder::checkProperty(QObject *obj, const QString
  //      &prop) const
  bool checkProperty(QObject *obj, const QString &prop) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQFormBuilderCall34 call = reinterpret_cast<CuteQFormBuilderCall34>(taken[34]);
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
    if (taken[35]) {
      int handled = 0;
      CuteQFormBuilderCall35 call = reinterpret_cast<CuteQFormBuilderCall35>(taken[35]);
      void * given = call(this, object, &propertyName, &value, &handled);
      if (handled) return static_cast<DomProperty *>(given);
    }
    return QAbstractFormBuilder::createProperty(object, propertyName, value);
  }
};

//  QFormBuilder::QFormBuilder()
extern "C" Q_DECL_EXPORT
QFormBuilder *ritual_ZN12QFormBuilderC1Ev() {
  return new CuteQFormBuilder();
}

//  QFormBuilder::~QFormBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFormBuilderD1Ev(QFormBuilder *self) {
  delete self;
}

//  QStringList QFormBuilder::pluginPaths() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK12QFormBuilder11pluginPathsEv(
    const QFormBuilder *self) {
  return new QList<QString>(self->pluginPaths());
}

//  void QFormBuilder::clearPluginPaths()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFormBuilder16clearPluginPathsEv(QFormBuilder *self) {
  self->clearPluginPaths();
}

//  void QFormBuilder::addPluginPath(const QString &pluginPath)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFormBuilder13addPluginPathERK7QString(
    QFormBuilder *self,
    const QString *pluginPath) {
  self->addPluginPath(*pluginPath);
}

//  void QFormBuilder::setPluginPath(const QStringList &pluginPaths)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFormBuilder13setPluginPathERK5QListI7QStringE(
    QFormBuilder *self,
    const QList<QString> *pluginPaths) {
  self->setPluginPath(*pluginPaths);
}

//  QList<QDesignerCustomWidgetInterface *> QFormBuilder::customWidgets()
//      const
extern "C" Q_DECL_EXPORT
QList<QDesignerCustomWidgetInterface *> *ritual_ZNK12QFormBuilder13customWidgetsEv(
    const QFormBuilder *self) {
  return new QList<QDesignerCustomWidgetInterface *>(self->customWidgets());
}

//  QWidget *QFormBuilder::create(DomUI *ui, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN12QFormBuilder6createEP5DomUIP7QWidget(
    QFormBuilder *self,
    DomUI *ui,
    QWidget *parentWidget) {
  return self->create(ui, parentWidget);
}

//  QWidget *QFormBuilder::create(DomWidget *ui_widget, QWidget
//      *parentWidget)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN12QFormBuilder6createEP9DomWidgetP7QWidget(
    QFormBuilder *self,
    DomWidget *ui_widget,
    QWidget *parentWidget) {
  return self->create(ui_widget, parentWidget);
}

//  QLayout *QFormBuilder::create(DomLayout *ui_layout, QLayout *layout,
//      QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QLayout *ritual_ZN12QFormBuilder6createEP9DomLayoutP7QLayoutP7QWidget(
    QFormBuilder *self,
    DomLayout *ui_layout,
    QLayout *layout,
    QWidget *parentWidget) {
  return self->create(ui_layout, layout, parentWidget);
}

//  QLayoutItem *QFormBuilder::create(DomLayoutItem *ui_layoutItem, QLayout
//      *layout, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN12QFormBuilder6createEP13DomLayoutItemP7QLayoutP7QWidget(
    QFormBuilder *self,
    DomLayoutItem *ui_layoutItem,
    QLayout *layout,
    QWidget *parentWidget) {
  return self->create(ui_layoutItem, layout, parentWidget);
}

//  QAction *QFormBuilder::create(DomAction *ui_action, QObject *parent)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN12QFormBuilder6createEP9DomActionP7QObject(
    QFormBuilder *self,
    DomAction *ui_action,
    QObject *parent) {
  return self->create(ui_action, parent);
}

//  QActionGroup *QFormBuilder::create(DomActionGroup *ui_action_group,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QActionGroup *ritual_ZN12QFormBuilder6createEP14DomActionGroupP7QObject(
    QFormBuilder *self,
    DomActionGroup *ui_action_group,
    QObject *parent) {
  return self->create(ui_action_group, parent);
}

//  QWidget *QFormBuilder::createWidget(const QString &widgetName, QWidget
//      *parentWidget, const QString &name)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN12QFormBuilder12createWidgetERK7QStringP7QWidgetS2_(
    QFormBuilder *self,
    const QString *widgetName,
    QWidget *parentWidget,
    const QString *name) {
  return self->createWidget(*widgetName, parentWidget, *name);
}

//  QLayout *QFormBuilder::createLayout(const QString &layoutName, QObject
//      *parent, const QString &name)
extern "C" Q_DECL_EXPORT
QLayout *ritual_ZN12QFormBuilder12createLayoutERK7QStringP7QObjectS2_(
    QFormBuilder *self,
    const QString *layoutName,
    QObject *parent,
    const QString *name) {
  return self->createLayout(*layoutName, parent, *name);
}

//  void QFormBuilder::createConnections(DomConnections *connections, QWidget
//      *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFormBuilder17createConnectionsEP14DomConnectionsP7QWidget(
    QFormBuilder *self,
    DomConnections *connections,
    QWidget *widget) {
  self->createConnections(connections, widget);
}

//  bool QFormBuilder::addItem(DomLayoutItem *ui_item, QLayoutItem *item,
//      QLayout *layout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QFormBuilder7addItemEP13DomLayoutItemP11QLayoutItemP7QLayout(
    QFormBuilder *self,
    DomLayoutItem *ui_item,
    QLayoutItem *item,
    QLayout *layout) {
  return self->addItem(ui_item, item, layout);
}

//  bool QFormBuilder::addItem(DomWidget *ui_widget, QWidget *widget, QWidget
//      *parentWidget)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QFormBuilder7addItemEP9DomWidgetP7QWidgetS3_(
    QFormBuilder *self,
    DomWidget *ui_widget,
    QWidget *widget,
    QWidget *parentWidget) {
  return self->addItem(ui_widget, widget, parentWidget);
}

//  void QFormBuilder::updateCustomWidgets()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFormBuilder19updateCustomWidgetsEv(QFormBuilder *self) {
  self->updateCustomWidgets();
}

//  void QFormBuilder::applyProperties(QObject *o, const QList<DomProperty *>
//      &properties)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFormBuilder15applyPropertiesEP7QObjectRK5QListIP11DomPropertyE(
    QFormBuilder *self,
    QObject *o,
    const QList<DomProperty *> *properties) {
  self->applyProperties(o, *properties);
}

//  QWidget *QFormBuilder::widgetByName(QWidget *topLevel, const QString
//      &name)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN12QFormBuilder12widgetByNameEP7QWidgetRK7QString(
    QWidget *topLevel,
    const QString *name) {
  return QFormBuilder::widgetByName(topLevel, *name);
}

//  a Python function taken by a CuteQFormBuilder, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFormBuilder(
    QFormBuilder *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFormBuilder *>(self)->take(key, call);
}

//  QWidget *QFormBuilder::create(DomUI *ui, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZN12QFormBuilder6createEP5DomUIP7QWidget(
    QFormBuilder *self,
    DomUI *ui,
    QWidget *parentWidget) {
  return static_cast<OwnQFormBuilder *>(self)->OwnQFormBuilder::create(
      ui,
      parentWidget);
}

//  QWidget *QFormBuilder::create(DomWidget *ui_widget, QWidget
//      *parentWidget)
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZN12QFormBuilder6createEP9DomWidgetP7QWidget(
    QFormBuilder *self,
    DomWidget *ui_widget,
    QWidget *parentWidget) {
  return static_cast<OwnQFormBuilder *>(self)->OwnQFormBuilder::create(
      ui_widget,
      parentWidget);
}

//  QLayout *QFormBuilder::create(DomLayout *ui_layout, QLayout *layout,
//      QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QLayout *ritual_own_ZN12QFormBuilder6createEP9DomLayoutP7QLayoutP7QWidget(
    QFormBuilder *self,
    DomLayout *ui_layout,
    QLayout *layout,
    QWidget *parentWidget) {
  return static_cast<OwnQFormBuilder *>(self)->OwnQFormBuilder::create(
      ui_layout,
      layout,
      parentWidget);
}

//  QLayoutItem *QFormBuilder::create(DomLayoutItem *ui_layoutItem, QLayout
//      *layout, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_own_ZN12QFormBuilder6createEP13DomLayoutItemP7QLayoutP7QWidget(
    QFormBuilder *self,
    DomLayoutItem *ui_layoutItem,
    QLayout *layout,
    QWidget *parentWidget) {
  return static_cast<OwnQFormBuilder *>(self)->OwnQFormBuilder::create(
      ui_layoutItem,
      layout,
      parentWidget);
}

//  QAction *QFormBuilder::create(DomAction *ui_action, QObject *parent)
extern "C" Q_DECL_EXPORT
QAction *ritual_own_ZN12QFormBuilder6createEP9DomActionP7QObject(
    QFormBuilder *self,
    DomAction *ui_action,
    QObject *parent) {
  return static_cast<OwnQFormBuilder *>(self)->OwnQFormBuilder::create(
      ui_action,
      parent);
}

//  QActionGroup *QFormBuilder::create(DomActionGroup *ui_action_group,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QActionGroup *ritual_own_ZN12QFormBuilder6createEP14DomActionGroupP7QObject(
    QFormBuilder *self,
    DomActionGroup *ui_action_group,
    QObject *parent) {
  return static_cast<OwnQFormBuilder *>(self)->OwnQFormBuilder::create(
      ui_action_group,
      parent);
}

//  QWidget *QFormBuilder::createWidget(const QString &widgetName, QWidget
//      *parentWidget, const QString &name)
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZN12QFormBuilder12createWidgetERK7QStringP7QWidgetS2_(
    QFormBuilder *self,
    const QString *widgetName,
    QWidget *parentWidget,
    const QString *name) {
  return static_cast<OwnQFormBuilder *>(self)->OwnQFormBuilder::createWidget(
      *widgetName,
      parentWidget,
      *name);
}

//  QLayout *QFormBuilder::createLayout(const QString &layoutName, QObject
//      *parent, const QString &name)
extern "C" Q_DECL_EXPORT
QLayout *ritual_own_ZN12QFormBuilder12createLayoutERK7QStringP7QObjectS2_(
    QFormBuilder *self,
    const QString *layoutName,
    QObject *parent,
    const QString *name) {
  return static_cast<OwnQFormBuilder *>(self)->OwnQFormBuilder::createLayout(
      *layoutName,
      parent,
      *name);
}

//  void QFormBuilder::createConnections(DomConnections *connections, QWidget
//      *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QFormBuilder17createConnectionsEP14DomConnectionsP7QWidget(
    QFormBuilder *self,
    DomConnections *connections,
    QWidget *widget) {
  static_cast<OwnQFormBuilder *>(self)->OwnQFormBuilder::createConnections(
      connections,
      widget);
}

//  bool QFormBuilder::addItem(DomLayoutItem *ui_item, QLayoutItem *item,
//      QLayout *layout)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QFormBuilder7addItemEP13DomLayoutItemP11QLayoutItemP7QLayout(
    QFormBuilder *self,
    DomLayoutItem *ui_item,
    QLayoutItem *item,
    QLayout *layout) {
  return static_cast<OwnQFormBuilder *>(self)->OwnQFormBuilder::addItem(
      ui_item,
      item,
      layout);
}

//  bool QFormBuilder::addItem(DomWidget *ui_widget, QWidget *widget, QWidget
//      *parentWidget)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QFormBuilder7addItemEP9DomWidgetP7QWidgetS3_(
    QFormBuilder *self,
    DomWidget *ui_widget,
    QWidget *widget,
    QWidget *parentWidget) {
  return static_cast<OwnQFormBuilder *>(self)->OwnQFormBuilder::addItem(
      ui_widget,
      widget,
      parentWidget);
}

//  void QFormBuilder::updateCustomWidgets()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QFormBuilder19updateCustomWidgetsEv(QFormBuilder *self) {
  static_cast<OwnQFormBuilder *>(self)->OwnQFormBuilder::updateCustomWidgets();
}
