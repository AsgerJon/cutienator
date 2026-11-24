//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractformbuilder.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/abstractformbuilder.h>
#include <QtCore/qdir.h>
#include <QtCore/qstring.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtGui/qpalette.h>
#include <QtGui/qbrush.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  Only a class built on QAbstractFormBuilder may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAbstractFormBuilder : QAbstractFormBuilder {
  using QAbstractFormBuilder::loadExtraInfo;
  using QAbstractFormBuilder::create;
  using QAbstractFormBuilder::addMenuAction;
  using QAbstractFormBuilder::applyTabStops;
  using QAbstractFormBuilder::createWidget;
  using QAbstractFormBuilder::createLayout;
  using QAbstractFormBuilder::createAction;
  using QAbstractFormBuilder::createActionGroup;
  using QAbstractFormBuilder::createCustomWidgets;
  using QAbstractFormBuilder::createConnections;
  using QAbstractFormBuilder::createResources;
  using QAbstractFormBuilder::addItem;
  using QAbstractFormBuilder::saveExtraInfo;
  using QAbstractFormBuilder::saveDom;
  using QAbstractFormBuilder::createActionRefDom;
  using QAbstractFormBuilder::createDom;
  using QAbstractFormBuilder::saveConnections;
  using QAbstractFormBuilder::saveCustomWidgets;
  using QAbstractFormBuilder::saveTabStops;
  using QAbstractFormBuilder::saveResources;
  using QAbstractFormBuilder::checkProperty;
  using QAbstractFormBuilder::createProperty;
};

//  A QAbstractFormBuilder that Python can take functions over in. Every QAbstractFormBuilder
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQAbstractFormBuilderCall0)(const void *, QIODevice *, QWidget *, int *);
typedef void (*CuteQAbstractFormBuilderCall1)(const void *, QIODevice *, QWidget *, int *);
typedef void (*CuteQAbstractFormBuilderCall2)(const void *, DomWidget *, QWidget *, QWidget *, int *);
typedef void * (*CuteQAbstractFormBuilderCall3)(const void *, DomUI *, QWidget *, int *);
typedef void * (*CuteQAbstractFormBuilderCall4)(const void *, DomWidget *, QWidget *, int *);
typedef void * (*CuteQAbstractFormBuilderCall5)(const void *, DomLayout *, QLayout *, QWidget *, int *);
typedef void * (*CuteQAbstractFormBuilderCall6)(const void *, DomLayoutItem *, QLayout *, QWidget *, int *);
typedef void * (*CuteQAbstractFormBuilderCall7)(const void *, DomAction *, QObject *, int *);
typedef void * (*CuteQAbstractFormBuilderCall8)(const void *, DomActionGroup *, QObject *, int *);
typedef void (*CuteQAbstractFormBuilderCall9)(const void *, QAction *, int *);
typedef void (*CuteQAbstractFormBuilderCall10)(const void *, QWidget *, DomTabStops *, int *);
typedef void * (*CuteQAbstractFormBuilderCall11)(const void *, const QString *, QWidget *, const QString *, int *);
typedef void * (*CuteQAbstractFormBuilderCall12)(const void *, const QString *, QObject *, const QString *, int *);
typedef void * (*CuteQAbstractFormBuilderCall13)(const void *, QObject *, const QString *, int *);
typedef void * (*CuteQAbstractFormBuilderCall14)(const void *, QObject *, const QString *, int *);
typedef void (*CuteQAbstractFormBuilderCall15)(const void *, DomCustomWidgets *, int *);
typedef void (*CuteQAbstractFormBuilderCall16)(const void *, DomConnections *, QWidget *, int *);
typedef void (*CuteQAbstractFormBuilderCall17)(const void *, DomResources *, int *);
typedef bool (*CuteQAbstractFormBuilderCall18)(const void *, DomLayoutItem *, QLayoutItem *, QLayout *, int *);
typedef bool (*CuteQAbstractFormBuilderCall19)(const void *, DomWidget *, QWidget *, QWidget *, int *);
typedef void (*CuteQAbstractFormBuilderCall20)(const void *, QWidget *, DomWidget *, DomWidget *, int *);
typedef void (*CuteQAbstractFormBuilderCall21)(const void *, DomUI *, QWidget *, int *);
typedef void * (*CuteQAbstractFormBuilderCall22)(const void *, QAction *, int *);
typedef void * (*CuteQAbstractFormBuilderCall23)(const void *, QWidget *, DomWidget *, bool, int *);
typedef void * (*CuteQAbstractFormBuilderCall24)(const void *, QLayout *, DomLayout *, DomWidget *, int *);
typedef void * (*CuteQAbstractFormBuilderCall25)(const void *, QLayoutItem *, DomLayout *, DomWidget *, int *);
typedef void * (*CuteQAbstractFormBuilderCall26)(const void *, QSpacerItem *, DomLayout *, DomWidget *, int *);
typedef void * (*CuteQAbstractFormBuilderCall27)(const void *, QAction *, int *);
typedef void * (*CuteQAbstractFormBuilderCall28)(const void *, QActionGroup *, int *);
typedef void * (*CuteQAbstractFormBuilderCall29)(const void *, int *);
typedef void * (*CuteQAbstractFormBuilderCall30)(const void *, int *);
typedef void * (*CuteQAbstractFormBuilderCall31)(const void *, int *);
typedef void * (*CuteQAbstractFormBuilderCall32)(const void *, int *);
typedef bool (*CuteQAbstractFormBuilderCall33)(const void *, QObject *, const QString *, int *);
typedef void * (*CuteQAbstractFormBuilderCall34)(const void *, QObject *, const QString *, const QVariant *, int *);
class CuteQAbstractFormBuilder : public QAbstractFormBuilder {
public:
  using QAbstractFormBuilder::QAbstractFormBuilder;
  void *taken[35] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder4loadEP9QIODeviceP7QWidget")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder4saveEP9QIODeviceP7QWidget")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder13loadExtraInfoEP9DomWidgetP7QWidgetS3_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder6createEP5DomUIP7QWidget")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder6createEP9DomWidgetP7QWidget")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder6createEP9DomLayoutP7QLayoutP7QWidget")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder6createEP13DomLayoutItemP7QLayoutP7QWidget")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder6createEP9DomActionP7QObject")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder6createEP14DomActionGroupP7QObject")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder13addMenuActionEP7QAction")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder13applyTabStopsEP7QWidgetP11DomTabStops")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder12createWidgetERK7QStringP7QWidgetS2_")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder12createLayoutERK7QStringP7QObjectS2_")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder12createActionEP7QObjectRK7QString")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder17createActionGroupEP7QObjectRK7QString")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder19createCustomWidgetsEP16DomCustomWidgets")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder17createConnectionsEP14DomConnectionsP7QWidget")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder15createResourcesEP12DomResources")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder7addItemEP13DomLayoutItemP11QLayoutItemP7QLayout")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder7addItemEP9DomWidgetP7QWidgetS3_")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder13saveExtraInfoEP7QWidgetP9DomWidgetS3_")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder7saveDomEP5DomUIP7QWidget")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder18createActionRefDomEP7QAction")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder9createDomEP7QWidgetP9DomWidgetb")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder9createDomEP7QLayoutP9DomLayoutP9DomWidget")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder9createDomEP11QLayoutItemP9DomLayoutP9DomWidget")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder9createDomEP11QSpacerItemP9DomLayoutP9DomWidget")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder9createDomEP7QAction")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder9createDomEP12QActionGroup")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder15saveConnectionsEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder17saveCustomWidgetsEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder12saveTabStopsEv")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder13saveResourcesEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QAbstractFormBuilder13checkPropertyEP7QObjectRK7QString")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractFormBuilder14createPropertyEP7QObjectRK7QStringRK8QVariant")) {
      taken[34] = call;
      return true;
    }
    return false;
  }

  //  QWidget *QAbstractFormBuilder::load(QIODevice *dev, QWidget
  //      *parentWidget)
  QWidget *load(QIODevice *dev, QWidget *parentWidget) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall0 call = reinterpret_cast<CuteQAbstractFormBuilderCall0>(taken[0]);
      void * given = call(this, dev, parentWidget, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QAbstractFormBuilder::load(dev, parentWidget);
  }

  //  void QAbstractFormBuilder::save(QIODevice *dev, QWidget *widget)
  void save(QIODevice *dev, QWidget *widget) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall1 call = reinterpret_cast<CuteQAbstractFormBuilderCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall2 call = reinterpret_cast<CuteQAbstractFormBuilderCall2>(taken[2]);
      call(this, ui_widget, widget, parentWidget, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::loadExtraInfo(ui_widget, widget, parentWidget);
  }

  //  QWidget *QAbstractFormBuilder::create(DomUI *ui, QWidget
  //      *parentWidget)
  QWidget *create(DomUI *ui, QWidget *parentWidget) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall3 call = reinterpret_cast<CuteQAbstractFormBuilderCall3>(taken[3]);
      void * given = call(this, ui, parentWidget, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QAbstractFormBuilder::create(ui, parentWidget);
  }

  //  QWidget *QAbstractFormBuilder::create(DomWidget *ui_widget, QWidget
  //      *parentWidget)
  QWidget *create(DomWidget *ui_widget, QWidget *parentWidget) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall4 call = reinterpret_cast<CuteQAbstractFormBuilderCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall5 call = reinterpret_cast<CuteQAbstractFormBuilderCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall6 call = reinterpret_cast<CuteQAbstractFormBuilderCall6>(taken[6]);
      void * given = call(this, ui_layoutItem, layout, parentWidget, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QAbstractFormBuilder::create(ui_layoutItem, layout, parentWidget);
  }

  //  QAction *QAbstractFormBuilder::create(DomAction *ui_action, QObject
  //      *parent)
  QAction *create(DomAction *ui_action, QObject *parent) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall7 call = reinterpret_cast<CuteQAbstractFormBuilderCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall8 call = reinterpret_cast<CuteQAbstractFormBuilderCall8>(taken[8]);
      void * given = call(this, ui_action_group, parent, &handled);
      if (handled) return static_cast<QActionGroup *>(given);
    }
    return QAbstractFormBuilder::create(ui_action_group, parent);
  }

  //  void QAbstractFormBuilder::addMenuAction(QAction *action)
  void addMenuAction(QAction *action) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall9 call = reinterpret_cast<CuteQAbstractFormBuilderCall9>(taken[9]);
      call(this, action, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::addMenuAction(action);
  }

  //  void QAbstractFormBuilder::applyTabStops(QWidget *widget, DomTabStops
  //      *tabStops)
  void applyTabStops(QWidget *widget, DomTabStops *tabStops) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall10 call = reinterpret_cast<CuteQAbstractFormBuilderCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall11 call = reinterpret_cast<CuteQAbstractFormBuilderCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall12 call = reinterpret_cast<CuteQAbstractFormBuilderCall12>(taken[12]);
      void * given = call(this, &layoutName, parent, &name, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return QAbstractFormBuilder::createLayout(layoutName, parent, name);
  }

  //  QAction *QAbstractFormBuilder::createAction(QObject *parent, const
  //      QString &name)
  QAction *createAction(QObject *parent, const QString &name) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall13 call = reinterpret_cast<CuteQAbstractFormBuilderCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall14 call = reinterpret_cast<CuteQAbstractFormBuilderCall14>(taken[14]);
      void * given = call(this, parent, &name, &handled);
      if (handled) return static_cast<QActionGroup *>(given);
    }
    return QAbstractFormBuilder::createActionGroup(parent, name);
  }

  //  void QAbstractFormBuilder::createCustomWidgets(DomCustomWidgets *a0)
  void createCustomWidgets(DomCustomWidgets *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall15 call = reinterpret_cast<CuteQAbstractFormBuilderCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::createCustomWidgets(a0);
  }

  //  void QAbstractFormBuilder::createConnections(DomConnections *a0,
  //      QWidget *a1)
  void createConnections(DomConnections *a0, QWidget *a1) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall16 call = reinterpret_cast<CuteQAbstractFormBuilderCall16>(taken[16]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::createConnections(a0, a1);
  }

  //  void QAbstractFormBuilder::createResources(DomResources *a0)
  void createResources(DomResources *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall17 call = reinterpret_cast<CuteQAbstractFormBuilderCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall18 call = reinterpret_cast<CuteQAbstractFormBuilderCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall19 call = reinterpret_cast<CuteQAbstractFormBuilderCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall20 call = reinterpret_cast<CuteQAbstractFormBuilderCall20>(taken[20]);
      call(this, widget, ui_widget, ui_parentWidget, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::saveExtraInfo(widget, ui_widget, ui_parentWidget);
  }

  //  void QAbstractFormBuilder::saveDom(DomUI *ui, QWidget *widget)
  void saveDom(DomUI *ui, QWidget *widget) override {
    if (taken[21]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall21 call = reinterpret_cast<CuteQAbstractFormBuilderCall21>(taken[21]);
      call(this, ui, widget, &handled);
      if (handled) return;
    }
    QAbstractFormBuilder::saveDom(ui, widget);
  }

  //  DomActionRef *QAbstractFormBuilder::createActionRefDom(QAction
  //      *action)
  DomActionRef *createActionRefDom(QAction *action) override {
    if (taken[22]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall22 call = reinterpret_cast<CuteQAbstractFormBuilderCall22>(taken[22]);
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
    if (taken[23]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall23 call = reinterpret_cast<CuteQAbstractFormBuilderCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall24 call = reinterpret_cast<CuteQAbstractFormBuilderCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall25 call = reinterpret_cast<CuteQAbstractFormBuilderCall25>(taken[25]);
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
    if (taken[26]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall26 call = reinterpret_cast<CuteQAbstractFormBuilderCall26>(taken[26]);
      void * given = call(this, spacer, ui_parentLayout, ui_parentWidget, &handled);
      if (handled) return static_cast<DomSpacer *>(given);
    }
    return QAbstractFormBuilder::createDom(spacer, ui_parentLayout, ui_parentWidget);
  }

  //  DomAction *QAbstractFormBuilder::createDom(QAction *action)
  DomAction *createDom(QAction *action) override {
    if (taken[27]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall27 call = reinterpret_cast<CuteQAbstractFormBuilderCall27>(taken[27]);
      void * given = call(this, action, &handled);
      if (handled) return static_cast<DomAction *>(given);
    }
    return QAbstractFormBuilder::createDom(action);
  }

  //  DomActionGroup *QAbstractFormBuilder::createDom(QActionGroup
  //      *actionGroup)
  DomActionGroup *createDom(QActionGroup *actionGroup) override {
    if (taken[28]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall28 call = reinterpret_cast<CuteQAbstractFormBuilderCall28>(taken[28]);
      void * given = call(this, actionGroup, &handled);
      if (handled) return static_cast<DomActionGroup *>(given);
    }
    return QAbstractFormBuilder::createDom(actionGroup);
  }

  //  DomConnections *QAbstractFormBuilder::saveConnections()
  DomConnections *saveConnections() override {
    if (taken[29]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall29 call = reinterpret_cast<CuteQAbstractFormBuilderCall29>(taken[29]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DomConnections *>(given);
    }
    return QAbstractFormBuilder::saveConnections();
  }

  //  DomCustomWidgets *QAbstractFormBuilder::saveCustomWidgets()
  DomCustomWidgets *saveCustomWidgets() override {
    if (taken[30]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall30 call = reinterpret_cast<CuteQAbstractFormBuilderCall30>(taken[30]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DomCustomWidgets *>(given);
    }
    return QAbstractFormBuilder::saveCustomWidgets();
  }

  //  DomTabStops *QAbstractFormBuilder::saveTabStops()
  DomTabStops *saveTabStops() override {
    if (taken[31]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall31 call = reinterpret_cast<CuteQAbstractFormBuilderCall31>(taken[31]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DomTabStops *>(given);
    }
    return QAbstractFormBuilder::saveTabStops();
  }

  //  DomResources *QAbstractFormBuilder::saveResources()
  DomResources *saveResources() override {
    if (taken[32]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall32 call = reinterpret_cast<CuteQAbstractFormBuilderCall32>(taken[32]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DomResources *>(given);
    }
    return QAbstractFormBuilder::saveResources();
  }

  //  bool QAbstractFormBuilder::checkProperty(QObject *obj, const QString
  //      &prop) const
  bool checkProperty(QObject *obj, const QString &prop) const override {
    if (taken[33]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall33 call = reinterpret_cast<CuteQAbstractFormBuilderCall33>(taken[33]);
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
    if (taken[34]) {
      int handled = 0;
      CuteQAbstractFormBuilderCall34 call = reinterpret_cast<CuteQAbstractFormBuilderCall34>(taken[34]);
      void * given = call(this, object, &propertyName, &value, &handled);
      if (handled) return static_cast<DomProperty *>(given);
    }
    return QAbstractFormBuilder::createProperty(object, propertyName, value);
  }
};

//  QAbstractFormBuilder::QAbstractFormBuilder()
extern "C" Q_DECL_EXPORT
QAbstractFormBuilder *ritual_ZN20QAbstractFormBuilderC1Ev() {
  return new CuteQAbstractFormBuilder();
}

//  QAbstractFormBuilder::~QAbstractFormBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilderD1Ev(QAbstractFormBuilder *self) {
  delete self;
}

//  QDir QAbstractFormBuilder::workingDirectory() const
extern "C" Q_DECL_EXPORT
QDir *ritual_ZNK20QAbstractFormBuilder16workingDirectoryEv(
    const QAbstractFormBuilder *self) {
  return new QDir(self->workingDirectory());
}

//  void QAbstractFormBuilder::setWorkingDirectory(const QDir &directory)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder19setWorkingDirectoryERK4QDir(
    QAbstractFormBuilder *self,
    const QDir *directory) {
  self->setWorkingDirectory(*directory);
}

//  QWidget *QAbstractFormBuilder::load(QIODevice *dev, QWidget
//      *parentWidget)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN20QAbstractFormBuilder4loadEP9QIODeviceP7QWidget(
    QAbstractFormBuilder *self,
    QIODevice *dev,
    QWidget *parentWidget) {
  return self->load(dev, parentWidget);
}

//  void QAbstractFormBuilder::save(QIODevice *dev, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder4saveEP9QIODeviceP7QWidget(
    QAbstractFormBuilder *self,
    QIODevice *dev,
    QWidget *widget) {
  self->save(dev, widget);
}

//  QString QAbstractFormBuilder::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QAbstractFormBuilder11errorStringEv(
    const QAbstractFormBuilder *self) {
  return new QString(self->errorString());
}

//  void QAbstractFormBuilder::loadExtraInfo(DomWidget *ui_widget, QWidget
//      *widget, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder13loadExtraInfoEP9DomWidgetP7QWidgetS3_(
    QAbstractFormBuilder *self,
    DomWidget *ui_widget,
    QWidget *widget,
    QWidget *parentWidget) {
  self->loadExtraInfo(ui_widget, widget, parentWidget);
}

//  QWidget *QAbstractFormBuilder::create(DomUI *ui, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN20QAbstractFormBuilder6createEP5DomUIP7QWidget(
    QAbstractFormBuilder *self,
    DomUI *ui,
    QWidget *parentWidget) {
  return self->create(ui, parentWidget);
}

//  QWidget *QAbstractFormBuilder::create(DomWidget *ui_widget, QWidget
//      *parentWidget)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN20QAbstractFormBuilder6createEP9DomWidgetP7QWidget(
    QAbstractFormBuilder *self,
    DomWidget *ui_widget,
    QWidget *parentWidget) {
  return self->create(ui_widget, parentWidget);
}

//  QLayout *QAbstractFormBuilder::create(DomLayout *ui_layout, QLayout
//      *layout, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QLayout *ritual_ZN20QAbstractFormBuilder6createEP9DomLayoutP7QLayoutP7QWidget(
    QAbstractFormBuilder *self,
    DomLayout *ui_layout,
    QLayout *layout,
    QWidget *parentWidget) {
  return self->create(ui_layout, layout, parentWidget);
}

//  QLayoutItem *QAbstractFormBuilder::create(DomLayoutItem *ui_layoutItem,
//      QLayout *layout, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN20QAbstractFormBuilder6createEP13DomLayoutItemP7QLayoutP7QWidget(
    QAbstractFormBuilder *self,
    DomLayoutItem *ui_layoutItem,
    QLayout *layout,
    QWidget *parentWidget) {
  return self->create(ui_layoutItem, layout, parentWidget);
}

//  QAction *QAbstractFormBuilder::create(DomAction *ui_action, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN20QAbstractFormBuilder6createEP9DomActionP7QObject(
    QAbstractFormBuilder *self,
    DomAction *ui_action,
    QObject *parent) {
  return self->create(ui_action, parent);
}

//  QActionGroup *QAbstractFormBuilder::create(DomActionGroup
//      *ui_action_group, QObject *parent)
extern "C" Q_DECL_EXPORT
QActionGroup *ritual_ZN20QAbstractFormBuilder6createEP14DomActionGroupP7QObject(
    QAbstractFormBuilder *self,
    DomActionGroup *ui_action_group,
    QObject *parent) {
  return self->create(ui_action_group, parent);
}

//  void QAbstractFormBuilder::addMenuAction(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder13addMenuActionEP7QAction(
    QAbstractFormBuilder *self,
    QAction *action) {
  self->addMenuAction(action);
}

//  void QAbstractFormBuilder::applyProperties(QObject *o, const
//      QList<DomProperty *> &properties)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder15applyPropertiesEP7QObjectRK5QListIP11DomPropertyE(
    QAbstractFormBuilder *self,
    QObject *o,
    const QList<DomProperty *> *properties) {
  self->applyProperties(o, *properties);
}

//  bool QAbstractFormBuilder::applyPropertyInternally(QObject *o, const
//      QString &propertyName, const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QAbstractFormBuilder23applyPropertyInternallyEP7QObjectRK7QStringRK8QVariant(
    QAbstractFormBuilder *self,
    QObject *o,
    const QString *propertyName,
    const QVariant *value) {
  return self->applyPropertyInternally(o, *propertyName, *value);
}

//  void QAbstractFormBuilder::applyTabStops(QWidget *widget, DomTabStops
//      *tabStops)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder13applyTabStopsEP7QWidgetP11DomTabStops(
    QAbstractFormBuilder *self,
    QWidget *widget,
    DomTabStops *tabStops) {
  self->applyTabStops(widget, tabStops);
}

//  QWidget *QAbstractFormBuilder::createWidget(const QString &widgetName,
//      QWidget *parentWidget, const QString &name)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN20QAbstractFormBuilder12createWidgetERK7QStringP7QWidgetS2_(
    QAbstractFormBuilder *self,
    const QString *widgetName,
    QWidget *parentWidget,
    const QString *name) {
  return self->createWidget(*widgetName, parentWidget, *name);
}

//  QLayout *QAbstractFormBuilder::createLayout(const QString &layoutName,
//      QObject *parent, const QString &name)
extern "C" Q_DECL_EXPORT
QLayout *ritual_ZN20QAbstractFormBuilder12createLayoutERK7QStringP7QObjectS2_(
    QAbstractFormBuilder *self,
    const QString *layoutName,
    QObject *parent,
    const QString *name) {
  return self->createLayout(*layoutName, parent, *name);
}

//  QAction *QAbstractFormBuilder::createAction(QObject *parent, const
//      QString &name)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN20QAbstractFormBuilder12createActionEP7QObjectRK7QString(
    QAbstractFormBuilder *self,
    QObject *parent,
    const QString *name) {
  return self->createAction(parent, *name);
}

//  QActionGroup *QAbstractFormBuilder::createActionGroup(QObject *parent,
//      const QString &name)
extern "C" Q_DECL_EXPORT
QActionGroup *ritual_ZN20QAbstractFormBuilder17createActionGroupEP7QObjectRK7QString(
    QAbstractFormBuilder *self,
    QObject *parent,
    const QString *name) {
  return self->createActionGroup(parent, *name);
}

//  void QAbstractFormBuilder::createCustomWidgets(DomCustomWidgets *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder19createCustomWidgetsEP16DomCustomWidgets(
    QAbstractFormBuilder *self,
    DomCustomWidgets *a0) {
  self->createCustomWidgets(a0);
}

//  void QAbstractFormBuilder::createConnections(DomConnections *a0, QWidget
//      *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder17createConnectionsEP14DomConnectionsP7QWidget(
    QAbstractFormBuilder *self,
    DomConnections *a0,
    QWidget *a1) {
  self->createConnections(a0, a1);
}

//  void QAbstractFormBuilder::createResources(DomResources *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder15createResourcesEP12DomResources(
    QAbstractFormBuilder *self,
    DomResources *a0) {
  self->createResources(a0);
}

//  bool QAbstractFormBuilder::addItem(DomLayoutItem *ui_item, QLayoutItem
//      *item, QLayout *layout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QAbstractFormBuilder7addItemEP13DomLayoutItemP11QLayoutItemP7QLayout(
    QAbstractFormBuilder *self,
    DomLayoutItem *ui_item,
    QLayoutItem *item,
    QLayout *layout) {
  return self->addItem(ui_item, item, layout);
}

//  bool QAbstractFormBuilder::addItem(DomWidget *ui_widget, QWidget *widget,
//      QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QAbstractFormBuilder7addItemEP9DomWidgetP7QWidgetS3_(
    QAbstractFormBuilder *self,
    DomWidget *ui_widget,
    QWidget *widget,
    QWidget *parentWidget) {
  return self->addItem(ui_widget, widget, parentWidget);
}

//  void QAbstractFormBuilder::saveExtraInfo(QWidget *widget, DomWidget
//      *ui_widget, DomWidget *ui_parentWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder13saveExtraInfoEP7QWidgetP9DomWidgetS3_(
    QAbstractFormBuilder *self,
    QWidget *widget,
    DomWidget *ui_widget,
    DomWidget *ui_parentWidget) {
  self->saveExtraInfo(widget, ui_widget, ui_parentWidget);
}

//  void QAbstractFormBuilder::saveDom(DomUI *ui, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder7saveDomEP5DomUIP7QWidget(
    QAbstractFormBuilder *self,
    DomUI *ui,
    QWidget *widget) {
  self->saveDom(ui, widget);
}

//  DomActionRef *QAbstractFormBuilder::createActionRefDom(QAction *action)
extern "C" Q_DECL_EXPORT
DomActionRef *ritual_ZN20QAbstractFormBuilder18createActionRefDomEP7QAction(
    QAbstractFormBuilder *self,
    QAction *action) {
  return self->createActionRefDom(action);
}

//  DomWidget *QAbstractFormBuilder::createDom(QWidget *widget, DomWidget
//      *ui_parentWidget, bool recursive)
extern "C" Q_DECL_EXPORT
DomWidget *ritual_ZN20QAbstractFormBuilder9createDomEP7QWidgetP9DomWidgetb(
    QAbstractFormBuilder *self,
    QWidget *widget,
    DomWidget *ui_parentWidget,
    bool recursive) {
  return self->createDom(widget, ui_parentWidget, recursive);
}

//  DomLayout *QAbstractFormBuilder::createDom(QLayout *layout, DomLayout
//      *ui_layout, DomWidget *ui_parentWidget)
extern "C" Q_DECL_EXPORT
DomLayout *ritual_ZN20QAbstractFormBuilder9createDomEP7QLayoutP9DomLayoutP9DomWidget(
    QAbstractFormBuilder *self,
    QLayout *layout,
    DomLayout *ui_layout,
    DomWidget *ui_parentWidget) {
  return self->createDom(layout, ui_layout, ui_parentWidget);
}

//  DomLayoutItem *QAbstractFormBuilder::createDom(QLayoutItem *item,
//      DomLayout *ui_parentLayout, DomWidget *ui_parentWidget)
extern "C" Q_DECL_EXPORT
DomLayoutItem *ritual_ZN20QAbstractFormBuilder9createDomEP11QLayoutItemP9DomLayoutP9DomWidget(
    QAbstractFormBuilder *self,
    QLayoutItem *item,
    DomLayout *ui_parentLayout,
    DomWidget *ui_parentWidget) {
  return self->createDom(item, ui_parentLayout, ui_parentWidget);
}

//  DomSpacer *QAbstractFormBuilder::createDom(QSpacerItem *spacer, DomLayout
//      *ui_parentLayout, DomWidget *ui_parentWidget)
extern "C" Q_DECL_EXPORT
DomSpacer *ritual_ZN20QAbstractFormBuilder9createDomEP11QSpacerItemP9DomLayoutP9DomWidget(
    QAbstractFormBuilder *self,
    QSpacerItem *spacer,
    DomLayout *ui_parentLayout,
    DomWidget *ui_parentWidget) {
  return self->createDom(spacer, ui_parentLayout, ui_parentWidget);
}

//  DomAction *QAbstractFormBuilder::createDom(QAction *action)
extern "C" Q_DECL_EXPORT
DomAction *ritual_ZN20QAbstractFormBuilder9createDomEP7QAction(
    QAbstractFormBuilder *self,
    QAction *action) {
  return self->createDom(action);
}

//  DomActionGroup *QAbstractFormBuilder::createDom(QActionGroup
//      *actionGroup)
extern "C" Q_DECL_EXPORT
DomActionGroup *ritual_ZN20QAbstractFormBuilder9createDomEP12QActionGroup(
    QAbstractFormBuilder *self,
    QActionGroup *actionGroup) {
  return self->createDom(actionGroup);
}

//  DomButtonGroup *QAbstractFormBuilder::createDom(QButtonGroup
//      *buttonGroup)
extern "C" Q_DECL_EXPORT
DomButtonGroup *ritual_ZN20QAbstractFormBuilder9createDomEP12QButtonGroup(
    QAbstractFormBuilder *self,
    QButtonGroup *buttonGroup) {
  return self->createDom(buttonGroup);
}

//  DomConnections *QAbstractFormBuilder::saveConnections()
extern "C" Q_DECL_EXPORT
DomConnections *ritual_ZN20QAbstractFormBuilder15saveConnectionsEv(
    QAbstractFormBuilder *self) {
  return self->saveConnections();
}

//  DomCustomWidgets *QAbstractFormBuilder::saveCustomWidgets()
extern "C" Q_DECL_EXPORT
DomCustomWidgets *ritual_ZN20QAbstractFormBuilder17saveCustomWidgetsEv(
    QAbstractFormBuilder *self) {
  return self->saveCustomWidgets();
}

//  DomTabStops *QAbstractFormBuilder::saveTabStops()
extern "C" Q_DECL_EXPORT
DomTabStops *ritual_ZN20QAbstractFormBuilder12saveTabStopsEv(
    QAbstractFormBuilder *self) {
  return self->saveTabStops();
}

//  DomResources *QAbstractFormBuilder::saveResources()
extern "C" Q_DECL_EXPORT
DomResources *ritual_ZN20QAbstractFormBuilder13saveResourcesEv(
    QAbstractFormBuilder *self) {
  return self->saveResources();
}

//  DomButtonGroups *QAbstractFormBuilder::saveButtonGroups(const QWidget
//      *mainContainer)
extern "C" Q_DECL_EXPORT
DomButtonGroups *ritual_ZN20QAbstractFormBuilder16saveButtonGroupsEPK7QWidget(
    QAbstractFormBuilder *self,
    const QWidget *mainContainer) {
  return self->saveButtonGroups(mainContainer);
}

//  QList<DomProperty *> QAbstractFormBuilder::computeProperties(QObject
//      *obj)
extern "C" Q_DECL_EXPORT
QList<DomProperty *> *ritual_ZN20QAbstractFormBuilder17computePropertiesEP7QObject(
    QAbstractFormBuilder *self,
    QObject *obj) {
  return new QList<DomProperty *>(self->computeProperties(obj));
}

//  bool QAbstractFormBuilder::checkProperty(QObject *obj, const QString
//      &prop) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QAbstractFormBuilder13checkPropertyEP7QObjectRK7QString(
    const QAbstractFormBuilder *self,
    QObject *obj,
    const QString *prop) {
  return self->checkProperty(obj, *prop);
}

//  DomProperty *QAbstractFormBuilder::createProperty(QObject *object, const
//      QString &propertyName, const QVariant &value)
extern "C" Q_DECL_EXPORT
DomProperty *ritual_ZN20QAbstractFormBuilder14createPropertyEP7QObjectRK7QStringRK8QVariant(
    QAbstractFormBuilder *self,
    QObject *object,
    const QString *propertyName,
    const QVariant *value) {
  return self->createProperty(object, *propertyName, *value);
}

//  void QAbstractFormBuilder::layoutInfo(DomLayout *layout, QObject *parent,
//      int *margin, int *spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder10layoutInfoEP9DomLayoutP7QObjectPiS4_(
    QAbstractFormBuilder *self,
    DomLayout *layout,
    QObject *parent,
    int *margin,
    int *spacing) {
  self->layoutInfo(layout, parent, margin, spacing);
}

//  void QAbstractFormBuilder::loadListWidgetExtraInfo(DomWidget *ui_widget,
//      QListWidget *listWidget, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder23loadListWidgetExtraInfoEP9DomWidgetP11QListWidgetP7QWidget(
    QAbstractFormBuilder *self,
    DomWidget *ui_widget,
    QListWidget *listWidget,
    QWidget *parentWidget) {
  self->loadListWidgetExtraInfo(ui_widget, listWidget, parentWidget);
}

//  void QAbstractFormBuilder::loadTreeWidgetExtraInfo(DomWidget *ui_widget,
//      QTreeWidget *treeWidget, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder23loadTreeWidgetExtraInfoEP9DomWidgetP11QTreeWidgetP7QWidget(
    QAbstractFormBuilder *self,
    DomWidget *ui_widget,
    QTreeWidget *treeWidget,
    QWidget *parentWidget) {
  self->loadTreeWidgetExtraInfo(ui_widget, treeWidget, parentWidget);
}

//  void QAbstractFormBuilder::loadTableWidgetExtraInfo(DomWidget *ui_widget,
//      QTableWidget *tableWidget, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder24loadTableWidgetExtraInfoEP9DomWidgetP12QTableWidgetP7QWidget(
    QAbstractFormBuilder *self,
    DomWidget *ui_widget,
    QTableWidget *tableWidget,
    QWidget *parentWidget) {
  self->loadTableWidgetExtraInfo(ui_widget, tableWidget, parentWidget);
}

//  void QAbstractFormBuilder::loadComboBoxExtraInfo(DomWidget *ui_widget,
//      QComboBox *comboBox, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder21loadComboBoxExtraInfoEP9DomWidgetP9QComboBoxP7QWidget(
    QAbstractFormBuilder *self,
    DomWidget *ui_widget,
    QComboBox *comboBox,
    QWidget *parentWidget) {
  self->loadComboBoxExtraInfo(ui_widget, comboBox, parentWidget);
}

//  void QAbstractFormBuilder::loadButtonExtraInfo(const DomWidget
//      *ui_widget, QAbstractButton *button, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder19loadButtonExtraInfoEPK9DomWidgetP15QAbstractButtonP7QWidget(
    QAbstractFormBuilder *self,
    const DomWidget *ui_widget,
    QAbstractButton *button,
    QWidget *parentWidget) {
  self->loadButtonExtraInfo(ui_widget, button, parentWidget);
}

//  void QAbstractFormBuilder::loadItemViewExtraInfo(DomWidget *ui_widget,
//      QAbstractItemView *itemView, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder21loadItemViewExtraInfoEP9DomWidgetP17QAbstractItemViewP7QWidget(
    QAbstractFormBuilder *self,
    DomWidget *ui_widget,
    QAbstractItemView *itemView,
    QWidget *parentWidget) {
  self->loadItemViewExtraInfo(ui_widget, itemView, parentWidget);
}

//  void QAbstractFormBuilder::saveListWidgetExtraInfo(QListWidget *widget,
//      DomWidget *ui_widget, DomWidget *ui_parentWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder23saveListWidgetExtraInfoEP11QListWidgetP9DomWidgetS3_(
    QAbstractFormBuilder *self,
    QListWidget *widget,
    DomWidget *ui_widget,
    DomWidget *ui_parentWidget) {
  self->saveListWidgetExtraInfo(widget, ui_widget, ui_parentWidget);
}

//  void QAbstractFormBuilder::saveTreeWidgetExtraInfo(QTreeWidget
//      *treeWidget, DomWidget *ui_widget, DomWidget *ui_parentWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder23saveTreeWidgetExtraInfoEP11QTreeWidgetP9DomWidgetS3_(
    QAbstractFormBuilder *self,
    QTreeWidget *treeWidget,
    DomWidget *ui_widget,
    DomWidget *ui_parentWidget) {
  self->saveTreeWidgetExtraInfo(treeWidget, ui_widget, ui_parentWidget);
}

//  void QAbstractFormBuilder::saveTableWidgetExtraInfo(QTableWidget
//      *tablWidget, DomWidget *ui_widget, DomWidget *ui_parentWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder24saveTableWidgetExtraInfoEP12QTableWidgetP9DomWidgetS3_(
    QAbstractFormBuilder *self,
    QTableWidget *tablWidget,
    DomWidget *ui_widget,
    DomWidget *ui_parentWidget) {
  self->saveTableWidgetExtraInfo(tablWidget, ui_widget, ui_parentWidget);
}

//  void QAbstractFormBuilder::saveComboBoxExtraInfo(QComboBox *widget,
//      DomWidget *ui_widget, DomWidget *ui_parentWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder21saveComboBoxExtraInfoEP9QComboBoxP9DomWidgetS3_(
    QAbstractFormBuilder *self,
    QComboBox *widget,
    DomWidget *ui_widget,
    DomWidget *ui_parentWidget) {
  self->saveComboBoxExtraInfo(widget, ui_widget, ui_parentWidget);
}

//  void QAbstractFormBuilder::saveButtonExtraInfo(const QAbstractButton
//      *widget, DomWidget *ui_widget, DomWidget *ui_parentWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder19saveButtonExtraInfoEPK15QAbstractButtonP9DomWidgetS4_(
    QAbstractFormBuilder *self,
    const QAbstractButton *widget,
    DomWidget *ui_widget,
    DomWidget *ui_parentWidget) {
  self->saveButtonExtraInfo(widget, ui_widget, ui_parentWidget);
}

//  void QAbstractFormBuilder::saveItemViewExtraInfo(const QAbstractItemView
//      *itemView, DomWidget *ui_widget, DomWidget *ui_parentWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder21saveItemViewExtraInfoEPK17QAbstractItemViewP9DomWidgetS4_(
    QAbstractFormBuilder *self,
    const QAbstractItemView *itemView,
    DomWidget *ui_widget,
    DomWidget *ui_parentWidget) {
  self->saveItemViewExtraInfo(itemView, ui_widget, ui_parentWidget);
}

//  void QAbstractFormBuilder::setResourceBuilder(QResourceBuilder *builder)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder18setResourceBuilderEP16QResourceBuilder(
    QAbstractFormBuilder *self,
    QResourceBuilder *builder) {
  self->setResourceBuilder(builder);
}

//  QResourceBuilder *QAbstractFormBuilder::resourceBuilder() const
extern "C" Q_DECL_EXPORT
QResourceBuilder *ritual_ZNK20QAbstractFormBuilder15resourceBuilderEv(
    const QAbstractFormBuilder *self) {
  return self->resourceBuilder();
}

//  DomProperty *QAbstractFormBuilder::saveResource(const QVariant &v) const
extern "C" Q_DECL_EXPORT
DomProperty *ritual_ZNK20QAbstractFormBuilder12saveResourceERK8QVariant(
    const QAbstractFormBuilder *self,
    const QVariant *v) {
  return self->saveResource(*v);
}

//  void QAbstractFormBuilder::setTextBuilder(QTextBuilder *builder)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder14setTextBuilderEP12QTextBuilder(
    QAbstractFormBuilder *self,
    QTextBuilder *builder) {
  self->setTextBuilder(builder);
}

//  QTextBuilder *QAbstractFormBuilder::textBuilder() const
extern "C" Q_DECL_EXPORT
QTextBuilder *ritual_ZNK20QAbstractFormBuilder11textBuilderEv(
    const QAbstractFormBuilder *self) {
  return self->textBuilder();
}

//  DomProperty *QAbstractFormBuilder::saveText(const QString &attributeName,
//      const QVariant &v) const
extern "C" Q_DECL_EXPORT
DomProperty *ritual_ZNK20QAbstractFormBuilder8saveTextERK7QStringRK8QVariant(
    const QAbstractFormBuilder *self,
    const QString *attributeName,
    const QVariant *v) {
  return self->saveText(*attributeName, *v);
}

//  QVariant QAbstractFormBuilder::toVariant(const QMetaObject *meta,
//      DomProperty *property)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN20QAbstractFormBuilder9toVariantEPK11QMetaObjectP11DomProperty(
    QAbstractFormBuilder *self,
    const QMetaObject *meta,
    DomProperty *property) {
  return new QVariant(self->toVariant(meta, property));
}

//  QString QAbstractFormBuilder::toString(const DomString *str)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QAbstractFormBuilder8toStringEPK9DomString(
    const DomString *str) {
  return new QString(QAbstractFormBuilder::toString(str));
}

//  DomPropertyHash QAbstractFormBuilder::propertyMap(const QList<DomProperty
//      *> &properties)
extern "C" Q_DECL_EXPORT
QHash<QString, DomProperty *> *ritual_ZN20QAbstractFormBuilder11propertyMapERK5QListIP11DomPropertyE(
    const QList<DomProperty *> *properties) {
  return new QHash<QString, DomProperty *>(
      QAbstractFormBuilder::propertyMap(
          *properties));
}

//  DomColorGroup *QAbstractFormBuilder::saveColorGroup(const QPalette
//      &palette)
extern "C" Q_DECL_EXPORT
DomColorGroup *ritual_ZN20QAbstractFormBuilder14saveColorGroupERK8QPalette(
    QAbstractFormBuilder *self,
    const QPalette *palette) {
  return self->saveColorGroup(*palette);
}

//  QBrush QAbstractFormBuilder::setupBrush(DomBrush *brush)
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN20QAbstractFormBuilder10setupBrushEP8DomBrush(
    QAbstractFormBuilder *self,
    DomBrush *brush) {
  return new QBrush(self->setupBrush(brush));
}

//  DomBrush *QAbstractFormBuilder::saveBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
DomBrush *ritual_ZN20QAbstractFormBuilder9saveBrushERK6QBrush(
    QAbstractFormBuilder *self,
    const QBrush *brush) {
  return self->saveBrush(*brush);
}

//  void QAbstractFormBuilder::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder5resetEv(QAbstractFormBuilder *self) {
  self->reset();
}

//  void QAbstractFormBuilder::initialize(const DomUI *ui)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractFormBuilder10initializeEPK5DomUI(
    QAbstractFormBuilder *self,
    const DomUI *ui) {
  self->initialize(ui);
}

//  QMetaEnum QAbstractFormBuilder::toolBarAreaMetaEnum()
extern "C" Q_DECL_EXPORT
QMetaEnum *ritual_ZN20QAbstractFormBuilder19toolBarAreaMetaEnumEv() {
  return new QMetaEnum(QAbstractFormBuilder::toolBarAreaMetaEnum());
}

//  const DomResourcePixmap *QAbstractFormBuilder::domPixmap(const
//      DomProperty *p)
extern "C" Q_DECL_EXPORT
const DomResourcePixmap *ritual_ZN20QAbstractFormBuilder9domPixmapEPK11DomProperty(
    const DomProperty *p) {
  return QAbstractFormBuilder::domPixmap(p);
}

//  Qt::ToolBarArea QAbstractFormBuilder::toolbarAreaFromDOMAttributes(const
//      DomPropertyHash &attributeMap)
extern "C" Q_DECL_EXPORT
Qt::ToolBarArea ritual_ZN20QAbstractFormBuilder28toolbarAreaFromDOMAttributesERK5QHashI7QStringP11DomPropertyE(
    const QHash<QString, DomProperty *> *attributeMap) {
  return QAbstractFormBuilder::toolbarAreaFromDOMAttributes(*attributeMap);
}

//  a Python function taken by a CuteQAbstractFormBuilder, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractFormBuilder(
    QAbstractFormBuilder *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractFormBuilder *>(self)->take(key, call);
}

//  QWidget *QAbstractFormBuilder::load(QIODevice *dev, QWidget
//      *parentWidget)
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZN20QAbstractFormBuilder4loadEP9QIODeviceP7QWidget(
    QAbstractFormBuilder *self,
    QIODevice *dev,
    QWidget *parentWidget) {
  return self->QAbstractFormBuilder::load(dev, parentWidget);
}

//  void QAbstractFormBuilder::save(QIODevice *dev, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAbstractFormBuilder4saveEP9QIODeviceP7QWidget(
    QAbstractFormBuilder *self,
    QIODevice *dev,
    QWidget *widget) {
  self->QAbstractFormBuilder::save(dev, widget);
}

//  void QAbstractFormBuilder::loadExtraInfo(DomWidget *ui_widget, QWidget
//      *widget, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAbstractFormBuilder13loadExtraInfoEP9DomWidgetP7QWidgetS3_(
    QAbstractFormBuilder *self,
    DomWidget *ui_widget,
    QWidget *widget,
    QWidget *parentWidget) {
  static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::loadExtraInfo(
      ui_widget,
      widget,
      parentWidget);
}

//  QWidget *QAbstractFormBuilder::create(DomUI *ui, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZN20QAbstractFormBuilder6createEP5DomUIP7QWidget(
    QAbstractFormBuilder *self,
    DomUI *ui,
    QWidget *parentWidget) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::create(
      ui,
      parentWidget);
}

//  QWidget *QAbstractFormBuilder::create(DomWidget *ui_widget, QWidget
//      *parentWidget)
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZN20QAbstractFormBuilder6createEP9DomWidgetP7QWidget(
    QAbstractFormBuilder *self,
    DomWidget *ui_widget,
    QWidget *parentWidget) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::create(
      ui_widget,
      parentWidget);
}

//  QLayout *QAbstractFormBuilder::create(DomLayout *ui_layout, QLayout
//      *layout, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QLayout *ritual_own_ZN20QAbstractFormBuilder6createEP9DomLayoutP7QLayoutP7QWidget(
    QAbstractFormBuilder *self,
    DomLayout *ui_layout,
    QLayout *layout,
    QWidget *parentWidget) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::create(
      ui_layout,
      layout,
      parentWidget);
}

//  QLayoutItem *QAbstractFormBuilder::create(DomLayoutItem *ui_layoutItem,
//      QLayout *layout, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_own_ZN20QAbstractFormBuilder6createEP13DomLayoutItemP7QLayoutP7QWidget(
    QAbstractFormBuilder *self,
    DomLayoutItem *ui_layoutItem,
    QLayout *layout,
    QWidget *parentWidget) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::create(
      ui_layoutItem,
      layout,
      parentWidget);
}

//  QAction *QAbstractFormBuilder::create(DomAction *ui_action, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QAction *ritual_own_ZN20QAbstractFormBuilder6createEP9DomActionP7QObject(
    QAbstractFormBuilder *self,
    DomAction *ui_action,
    QObject *parent) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::create(
      ui_action,
      parent);
}

//  QActionGroup *QAbstractFormBuilder::create(DomActionGroup
//      *ui_action_group, QObject *parent)
extern "C" Q_DECL_EXPORT
QActionGroup *ritual_own_ZN20QAbstractFormBuilder6createEP14DomActionGroupP7QObject(
    QAbstractFormBuilder *self,
    DomActionGroup *ui_action_group,
    QObject *parent) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::create(
      ui_action_group,
      parent);
}

//  void QAbstractFormBuilder::addMenuAction(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAbstractFormBuilder13addMenuActionEP7QAction(
    QAbstractFormBuilder *self,
    QAction *action) {
  static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::addMenuAction(
      action);
}

//  void QAbstractFormBuilder::applyTabStops(QWidget *widget, DomTabStops
//      *tabStops)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAbstractFormBuilder13applyTabStopsEP7QWidgetP11DomTabStops(
    QAbstractFormBuilder *self,
    QWidget *widget,
    DomTabStops *tabStops) {
  static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::applyTabStops(
      widget,
      tabStops);
}

//  QWidget *QAbstractFormBuilder::createWidget(const QString &widgetName,
//      QWidget *parentWidget, const QString &name)
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZN20QAbstractFormBuilder12createWidgetERK7QStringP7QWidgetS2_(
    QAbstractFormBuilder *self,
    const QString *widgetName,
    QWidget *parentWidget,
    const QString *name) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::createWidget(
      *widgetName,
      parentWidget,
      *name);
}

//  QLayout *QAbstractFormBuilder::createLayout(const QString &layoutName,
//      QObject *parent, const QString &name)
extern "C" Q_DECL_EXPORT
QLayout *ritual_own_ZN20QAbstractFormBuilder12createLayoutERK7QStringP7QObjectS2_(
    QAbstractFormBuilder *self,
    const QString *layoutName,
    QObject *parent,
    const QString *name) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::createLayout(
      *layoutName,
      parent,
      *name);
}

//  QAction *QAbstractFormBuilder::createAction(QObject *parent, const
//      QString &name)
extern "C" Q_DECL_EXPORT
QAction *ritual_own_ZN20QAbstractFormBuilder12createActionEP7QObjectRK7QString(
    QAbstractFormBuilder *self,
    QObject *parent,
    const QString *name) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::createAction(
      parent,
      *name);
}

//  QActionGroup *QAbstractFormBuilder::createActionGroup(QObject *parent,
//      const QString &name)
extern "C" Q_DECL_EXPORT
QActionGroup *ritual_own_ZN20QAbstractFormBuilder17createActionGroupEP7QObjectRK7QString(
    QAbstractFormBuilder *self,
    QObject *parent,
    const QString *name) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::createActionGroup(
      parent,
      *name);
}

//  void QAbstractFormBuilder::createCustomWidgets(DomCustomWidgets *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAbstractFormBuilder19createCustomWidgetsEP16DomCustomWidgets(
    QAbstractFormBuilder *self,
    DomCustomWidgets *a0) {
  static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::createCustomWidgets(
      a0);
}

//  void QAbstractFormBuilder::createConnections(DomConnections *a0, QWidget
//      *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAbstractFormBuilder17createConnectionsEP14DomConnectionsP7QWidget(
    QAbstractFormBuilder *self,
    DomConnections *a0,
    QWidget *a1) {
  static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::createConnections(
      a0,
      a1);
}

//  void QAbstractFormBuilder::createResources(DomResources *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAbstractFormBuilder15createResourcesEP12DomResources(
    QAbstractFormBuilder *self,
    DomResources *a0) {
  static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::createResources(
      a0);
}

//  bool QAbstractFormBuilder::addItem(DomLayoutItem *ui_item, QLayoutItem
//      *item, QLayout *layout)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QAbstractFormBuilder7addItemEP13DomLayoutItemP11QLayoutItemP7QLayout(
    QAbstractFormBuilder *self,
    DomLayoutItem *ui_item,
    QLayoutItem *item,
    QLayout *layout) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::addItem(
      ui_item,
      item,
      layout);
}

//  bool QAbstractFormBuilder::addItem(DomWidget *ui_widget, QWidget *widget,
//      QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QAbstractFormBuilder7addItemEP9DomWidgetP7QWidgetS3_(
    QAbstractFormBuilder *self,
    DomWidget *ui_widget,
    QWidget *widget,
    QWidget *parentWidget) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::addItem(
      ui_widget,
      widget,
      parentWidget);
}

//  void QAbstractFormBuilder::saveExtraInfo(QWidget *widget, DomWidget
//      *ui_widget, DomWidget *ui_parentWidget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAbstractFormBuilder13saveExtraInfoEP7QWidgetP9DomWidgetS3_(
    QAbstractFormBuilder *self,
    QWidget *widget,
    DomWidget *ui_widget,
    DomWidget *ui_parentWidget) {
  static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::saveExtraInfo(
      widget,
      ui_widget,
      ui_parentWidget);
}

//  void QAbstractFormBuilder::saveDom(DomUI *ui, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAbstractFormBuilder7saveDomEP5DomUIP7QWidget(
    QAbstractFormBuilder *self,
    DomUI *ui,
    QWidget *widget) {
  static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::saveDom(
      ui,
      widget);
}

//  DomActionRef *QAbstractFormBuilder::createActionRefDom(QAction *action)
extern "C" Q_DECL_EXPORT
DomActionRef *ritual_own_ZN20QAbstractFormBuilder18createActionRefDomEP7QAction(
    QAbstractFormBuilder *self,
    QAction *action) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::createActionRefDom(
      action);
}

//  DomWidget *QAbstractFormBuilder::createDom(QWidget *widget, DomWidget
//      *ui_parentWidget, bool recursive)
extern "C" Q_DECL_EXPORT
DomWidget *ritual_own_ZN20QAbstractFormBuilder9createDomEP7QWidgetP9DomWidgetb(
    QAbstractFormBuilder *self,
    QWidget *widget,
    DomWidget *ui_parentWidget,
    bool recursive) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::createDom(
      widget,
      ui_parentWidget,
      recursive);
}

//  DomLayout *QAbstractFormBuilder::createDom(QLayout *layout, DomLayout
//      *ui_layout, DomWidget *ui_parentWidget)
extern "C" Q_DECL_EXPORT
DomLayout *ritual_own_ZN20QAbstractFormBuilder9createDomEP7QLayoutP9DomLayoutP9DomWidget(
    QAbstractFormBuilder *self,
    QLayout *layout,
    DomLayout *ui_layout,
    DomWidget *ui_parentWidget) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::createDom(
      layout,
      ui_layout,
      ui_parentWidget);
}

//  DomLayoutItem *QAbstractFormBuilder::createDom(QLayoutItem *item,
//      DomLayout *ui_parentLayout, DomWidget *ui_parentWidget)
extern "C" Q_DECL_EXPORT
DomLayoutItem *ritual_own_ZN20QAbstractFormBuilder9createDomEP11QLayoutItemP9DomLayoutP9DomWidget(
    QAbstractFormBuilder *self,
    QLayoutItem *item,
    DomLayout *ui_parentLayout,
    DomWidget *ui_parentWidget) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::createDom(
      item,
      ui_parentLayout,
      ui_parentWidget);
}

//  DomSpacer *QAbstractFormBuilder::createDom(QSpacerItem *spacer, DomLayout
//      *ui_parentLayout, DomWidget *ui_parentWidget)
extern "C" Q_DECL_EXPORT
DomSpacer *ritual_own_ZN20QAbstractFormBuilder9createDomEP11QSpacerItemP9DomLayoutP9DomWidget(
    QAbstractFormBuilder *self,
    QSpacerItem *spacer,
    DomLayout *ui_parentLayout,
    DomWidget *ui_parentWidget) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::createDom(
      spacer,
      ui_parentLayout,
      ui_parentWidget);
}

//  DomAction *QAbstractFormBuilder::createDom(QAction *action)
extern "C" Q_DECL_EXPORT
DomAction *ritual_own_ZN20QAbstractFormBuilder9createDomEP7QAction(
    QAbstractFormBuilder *self,
    QAction *action) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::createDom(
      action);
}

//  DomActionGroup *QAbstractFormBuilder::createDom(QActionGroup
//      *actionGroup)
extern "C" Q_DECL_EXPORT
DomActionGroup *ritual_own_ZN20QAbstractFormBuilder9createDomEP12QActionGroup(
    QAbstractFormBuilder *self,
    QActionGroup *actionGroup) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::createDom(
      actionGroup);
}

//  DomConnections *QAbstractFormBuilder::saveConnections()
extern "C" Q_DECL_EXPORT
DomConnections *ritual_own_ZN20QAbstractFormBuilder15saveConnectionsEv(
    QAbstractFormBuilder *self) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::saveConnections();
}

//  DomCustomWidgets *QAbstractFormBuilder::saveCustomWidgets()
extern "C" Q_DECL_EXPORT
DomCustomWidgets *ritual_own_ZN20QAbstractFormBuilder17saveCustomWidgetsEv(
    QAbstractFormBuilder *self) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::saveCustomWidgets();
}

//  DomTabStops *QAbstractFormBuilder::saveTabStops()
extern "C" Q_DECL_EXPORT
DomTabStops *ritual_own_ZN20QAbstractFormBuilder12saveTabStopsEv(
    QAbstractFormBuilder *self) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::saveTabStops();
}

//  DomResources *QAbstractFormBuilder::saveResources()
extern "C" Q_DECL_EXPORT
DomResources *ritual_own_ZN20QAbstractFormBuilder13saveResourcesEv(
    QAbstractFormBuilder *self) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::saveResources();
}

//  bool QAbstractFormBuilder::checkProperty(QObject *obj, const QString
//      &prop) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QAbstractFormBuilder13checkPropertyEP7QObjectRK7QString(
    const QAbstractFormBuilder *self,
    QObject *obj,
    const QString *prop) {
  return static_cast<const OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::checkProperty(
      obj,
      *prop);
}

//  DomProperty *QAbstractFormBuilder::createProperty(QObject *object, const
//      QString &propertyName, const QVariant &value)
extern "C" Q_DECL_EXPORT
DomProperty *ritual_own_ZN20QAbstractFormBuilder14createPropertyEP7QObjectRK7QStringRK8QVariant(
    QAbstractFormBuilder *self,
    QObject *object,
    const QString *propertyName,
    const QVariant *value) {
  return static_cast<OwnQAbstractFormBuilder *>(self)->OwnQAbstractFormBuilder::createProperty(
      object,
      *propertyName,
      *value);
}
