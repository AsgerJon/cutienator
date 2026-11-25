//  Written by hand on 2026-11-25 from
//  QtDataVisualizationQml/6.12.0/QtDataVisualizationQml/private/
//  abstractdeclarative_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  The part has no global or exports header of its own (its
//  CMakeLists.txt says NO_GENERATE_CPP_EXPORTS): those of
//  QtDataVisualization, on which it is built, come first.
//  Qt's library offers nothing of this class by name: its class line
//  has no export macro. Written: its virtual functions, called
//  through the object, metaObject() and the destructor among them,
//  and its inline functions 'mutex', 'isReady' and the marker
//  QML_UNCREATABLE gives it. 'wheelEvent' stands under
//  QT_CONFIG(wheelevent), as Qt declares it.
//  Not written: the constructor and 'tr'; the signals; and the
//  functions neither virtual nor inline, which Qt's library offers
//  not, 'customItemList' and the static '...CustomItemFunc' among
//  them; nor the operators Q_DECLARE_OPERATORS_FOR_FLAGS declares,
//  which are not the class's.
#include <QtDataVisualization/qdatavisualizationglobal.h>
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualizationQml/6.12.0/QtDataVisualizationQml/private/abstractdeclarative_p.h>
#include <QtCore/qmutex.h>
#include <QtCore/qrect.h>
#include <QtGui/qevent.h>
#include <QtGui/qvectornd.h>
#include <QtQuick/qquickwindow.h>
#include <QtQuick/qsgnode.h>

//  const QMetaObject *AbstractDeclarative::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19AbstractDeclarative10metaObjectEv(
    const AbstractDeclarative *self) {
  return self->metaObject();
}

//  AbstractDeclarative::~AbstractDeclarative()
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarativeD1Ev(AbstractDeclarative *self) {
  delete self;
}

//  void AbstractDeclarative::setRenderingMode(RenderingMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative16setRenderingModeENS_13RenderingModeE(
    AbstractDeclarative *self,
    AbstractDeclarative::RenderingMode mode) {
  self->setRenderingMode(mode);
}

//  AbstractDeclarative::RenderingMode AbstractDeclarative::renderingMode()
//      const
extern "C" Q_DECL_EXPORT
AbstractDeclarative::RenderingMode ritual_ZNK19AbstractDeclarative13renderingModeEv(
    const AbstractDeclarative *self) {
  return self->renderingMode();
}

//  void AbstractDeclarative::setSelectionMode(SelectionFlags mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative16setSelectionModeE6QFlagsINS_13SelectionFlagEE(
    AbstractDeclarative *self,
    int mode) {
  self->setSelectionMode(
      QFlags<AbstractDeclarative::SelectionFlag>::fromInt(mode));
}

//  AbstractDeclarative::SelectionFlags AbstractDeclarative::selectionMode()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19AbstractDeclarative13selectionModeEv(
    const AbstractDeclarative *self) {
  return static_cast<int>(self->selectionMode().toInt());
}

//  void AbstractDeclarative::setShadowQuality(ShadowQuality quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative16setShadowQualityENS_13ShadowQualityE(
    AbstractDeclarative *self,
    AbstractDeclarative::ShadowQuality quality) {
  self->setShadowQuality(quality);
}

//  AbstractDeclarative::ShadowQuality AbstractDeclarative::shadowQuality()
//      const
extern "C" Q_DECL_EXPORT
AbstractDeclarative::ShadowQuality ritual_ZNK19AbstractDeclarative13shadowQualityEv(
    const AbstractDeclarative *self) {
  return self->shadowQuality();
}

//  AbstractDeclarative::ElementType AbstractDeclarative::selectedElement()
//      const
extern "C" Q_DECL_EXPORT
AbstractDeclarative::ElementType ritual_ZNK19AbstractDeclarative15selectedElementEv(
    const AbstractDeclarative *self) {
  return self->selectedElement();
}

//  bool AbstractDeclarative::shadowsSupported() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19AbstractDeclarative16shadowsSupportedEv(
    const AbstractDeclarative *self) {
  return self->shadowsSupported();
}

//  void AbstractDeclarative::setMsaaSamples(int samples)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative14setMsaaSamplesEi(
    AbstractDeclarative *self,
    int samples) {
  self->setMsaaSamples(samples);
}

//  int AbstractDeclarative::msaaSamples() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19AbstractDeclarative11msaaSamplesEv(
    const AbstractDeclarative *self) {
  return self->msaaSamples();
}

//  Declarative3DScene *AbstractDeclarative::scene() const
extern "C" Q_DECL_EXPORT
Declarative3DScene *ritual_ZNK19AbstractDeclarative5sceneEv(
    const AbstractDeclarative *self) {
  return self->scene();
}

//  QAbstract3DInputHandler *AbstractDeclarative::inputHandler() const
extern "C" Q_DECL_EXPORT
QAbstract3DInputHandler *ritual_ZNK19AbstractDeclarative12inputHandlerEv(
    const AbstractDeclarative *self) {
  return self->inputHandler();
}

//  void AbstractDeclarative::setInputHandler(QAbstract3DInputHandler
//      *inputHandler)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative15setInputHandlerEP23QAbstract3DInputHandler(
    AbstractDeclarative *self,
    QAbstract3DInputHandler *inputHandler) {
  self->setInputHandler(inputHandler);
}

//  void AbstractDeclarative::setTheme(Q3DTheme *theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative8setThemeEP8Q3DTheme(
    AbstractDeclarative *self,
    Q3DTheme *theme) {
  self->setTheme(theme);
}

//  Q3DTheme *AbstractDeclarative::theme() const
extern "C" Q_DECL_EXPORT
Q3DTheme *ritual_ZNK19AbstractDeclarative5themeEv(
    const AbstractDeclarative *self) {
  return self->theme();
}

//  void AbstractDeclarative::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative14clearSelectionEv(
    AbstractDeclarative *self) {
  self->clearSelection();
}

//  bool AbstractDeclarative::hasSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19AbstractDeclarative9hasSeriesEP17QAbstract3DSeries(
    AbstractDeclarative *self,
    QAbstract3DSeries *series) {
  return self->hasSeries(series);
}

//  int AbstractDeclarative::addCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
int ritual_ZN19AbstractDeclarative13addCustomItemEP13QCustom3DItem(
    AbstractDeclarative *self,
    QCustom3DItem *item) {
  return self->addCustomItem(item);
}

//  void AbstractDeclarative::removeCustomItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative17removeCustomItemsEv(
    AbstractDeclarative *self) {
  self->removeCustomItems();
}

//  void AbstractDeclarative::removeCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative16removeCustomItemEP13QCustom3DItem(
    AbstractDeclarative *self,
    QCustom3DItem *item) {
  self->removeCustomItem(item);
}

//  void AbstractDeclarative::removeCustomItemAt(const QVector3D &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative18removeCustomItemAtERK9QVector3D(
    AbstractDeclarative *self,
    const QVector3D *position) {
  self->removeCustomItemAt(*position);
}

//  void AbstractDeclarative::releaseCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative17releaseCustomItemEP13QCustom3DItem(
    AbstractDeclarative *self,
    QCustom3DItem *item) {
  self->releaseCustomItem(item);
}

//  int AbstractDeclarative::selectedLabelIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19AbstractDeclarative18selectedLabelIndexEv(
    const AbstractDeclarative *self) {
  return self->selectedLabelIndex();
}

//  QAbstract3DAxis *AbstractDeclarative::selectedAxis() const
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZNK19AbstractDeclarative12selectedAxisEv(
    const AbstractDeclarative *self) {
  return self->selectedAxis();
}

//  int AbstractDeclarative::selectedCustomItemIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19AbstractDeclarative23selectedCustomItemIndexEv(
    const AbstractDeclarative *self) {
  return self->selectedCustomItemIndex();
}

//  QCustom3DItem *AbstractDeclarative::selectedCustomItem() const
extern "C" Q_DECL_EXPORT
QCustom3DItem *ritual_ZNK19AbstractDeclarative18selectedCustomItemEv(
    const AbstractDeclarative *self) {
  return self->selectedCustomItem();
}

//  void AbstractDeclarative::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative14geometryChangeERK6QRectFS2_(
    AbstractDeclarative *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  QMutex *AbstractDeclarative::mutex()
extern "C" Q_DECL_EXPORT
QMutex *ritual_ZN19AbstractDeclarative5mutexEv(AbstractDeclarative *self) {
  return self->mutex();
}

//  bool AbstractDeclarative::isReady() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19AbstractDeclarative7isReadyEv(
    const AbstractDeclarative *self) {
  return self->isReady();
}

//  void AbstractDeclarative::handleAxisXChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative18handleAxisXChangedEP15QAbstract3DAxis(
    AbstractDeclarative *self,
    QAbstract3DAxis *axis) {
  self->handleAxisXChanged(axis);
}

//  void AbstractDeclarative::handleAxisYChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative18handleAxisYChangedEP15QAbstract3DAxis(
    AbstractDeclarative *self,
    QAbstract3DAxis *axis) {
  self->handleAxisYChanged(axis);
}

//  void AbstractDeclarative::handleAxisZChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative18handleAxisZChangedEP15QAbstract3DAxis(
    AbstractDeclarative *self,
    QAbstract3DAxis *axis) {
  self->handleAxisZChanged(axis);
}

//  void AbstractDeclarative::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative21mouseDoubleClickEventEP11QMouseEvent(
    AbstractDeclarative *self,
    QMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void AbstractDeclarative::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative10touchEventEP11QTouchEvent(
    AbstractDeclarative *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}

//  void AbstractDeclarative::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative15mousePressEventEP11QMouseEvent(
    AbstractDeclarative *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void AbstractDeclarative::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative17mouseReleaseEventEP11QMouseEvent(
    AbstractDeclarative *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void AbstractDeclarative::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative14mouseMoveEventEP11QMouseEvent(
    AbstractDeclarative *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

#if QT_CONFIG(wheelevent)
//  void AbstractDeclarative::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative10wheelEventEP11QWheelEvent(
    AbstractDeclarative *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  void AbstractDeclarative::handleWindowChanged(QQuickWindow *win)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative19handleWindowChangedEP12QQuickWindow(
    AbstractDeclarative *self,
    QQuickWindow *win) {
  self->handleWindowChanged(win);
}

//  void AbstractDeclarative::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    AbstractDeclarative *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void AbstractDeclarative::updateWindowParameters()
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative22updateWindowParametersEv(
    AbstractDeclarative *self) {
  self->updateWindowParameters();
}

//  void AbstractDeclarative::handleSelectionModeChange(
//      QAbstract3DGraph::SelectionFlags mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative25handleSelectionModeChangeE6QFlagsIN16QAbstract3DGraph13SelectionFlagEE(
    AbstractDeclarative *self,
    int mode) {
  self->handleSelectionModeChange(
      QFlags<QAbstract3DGraph::SelectionFlag>::fromInt(mode));
}

//  void AbstractDeclarative::handleShadowQualityChange(
//      QAbstract3DGraph::ShadowQuality quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative25handleShadowQualityChangeEN16QAbstract3DGraph13ShadowQualityE(
    AbstractDeclarative *self,
    QAbstract3DGraph::ShadowQuality quality) {
  self->handleShadowQualityChange(quality);
}

//  void AbstractDeclarative::handleSelectedElementChange(
//      QAbstract3DGraph::ElementType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative27handleSelectedElementChangeEN16QAbstract3DGraph11ElementTypeE(
    AbstractDeclarative *self,
    QAbstract3DGraph::ElementType type) {
  self->handleSelectedElementChange(type);
}

//  void AbstractDeclarative::handleOptimizationHintChange(
//      QAbstract3DGraph::OptimizationHints hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractDeclarative28handleOptimizationHintChangeE6QFlagsIN16QAbstract3DGraph16OptimizationHintEE(
    AbstractDeclarative *self,
    int hints) {
  self->handleOptimizationHintChange(
      QFlags<QAbstract3DGraph::OptimizationHint>::fromInt(hints));
}

//  QSGNode *AbstractDeclarative::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN19AbstractDeclarative15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    AbstractDeclarative *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(oldNode, a1);
}
