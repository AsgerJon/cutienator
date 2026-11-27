//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineQui
//  ck/6.12.0/QtWebEngineQuick/private/qquickwebenginefaviconprovider_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginefaviconprovider_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/QPointer>
#include <QtCore/QUrl>

//  const QMetaObject *FaviconProviderHelper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21FaviconProviderHelper10metaObjectEv(
    const FaviconProviderHelper *self) {
  return self->metaObject();
}

//  void *FaviconProviderHelper::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21FaviconProviderHelper11qt_metacastEPKc(
    FaviconProviderHelper *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int FaviconProviderHelper::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21FaviconProviderHelper11qt_metacallEN11QMetaObject4CallEiPPv(
    FaviconProviderHelper *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString FaviconProviderHelper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21FaviconProviderHelper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(FaviconProviderHelper::tr(s, c, n));
}

//  FaviconProviderHelper *FaviconProviderHelper::instance()
extern "C" Q_DECL_EXPORT
FaviconProviderHelper *ritual_ZN21FaviconProviderHelper8instanceEv() {
  return FaviconProviderHelper::instance();
}

//  void FaviconProviderHelper::attach(QPointer<QQuickWebEngineView> view)
extern "C" Q_DECL_EXPORT
void ritual_ZN21FaviconProviderHelper6attachE8QPointerI19QQuickWebEngineViewE(
    FaviconProviderHelper *self,
    const QPointer<QQuickWebEngineView> *view) {
  self->attach(*view);
}

//  void FaviconProviderHelper::detach(QPointer<QQuickWebEngineView> view)
extern "C" Q_DECL_EXPORT
void ritual_ZN21FaviconProviderHelper6detachE8QPointerI19QQuickWebEngineViewE(
    FaviconProviderHelper *self,
    const QPointer<QQuickWebEngineView> *view) {
  self->detach(*view);
}

//  const QList<QPointer<QQuickWebEngineView>>
//      &FaviconProviderHelper::views() const
extern "C" Q_DECL_EXPORT
const QList<QPointer<QQuickWebEngineView>> *ritual_ZNK21FaviconProviderHelper5viewsEv(
    const FaviconProviderHelper *self) {
  return &(self->views());
}

//  void
//      FaviconProviderHelper::handleImageRequest(QPointer<FaviconImageRespon
//      se> faviconResponse)
extern "C" Q_DECL_EXPORT
void ritual_ZN21FaviconProviderHelper18handleImageRequestE8QPointerI20FaviconImageResponseE(
    FaviconProviderHelper *self,
    const QPointer<FaviconImageResponse> *faviconResponse) {
  self->handleImageRequest(*faviconResponse);
}

//  FaviconProviderHelper::FaviconProviderHelper()
extern "C" Q_DECL_EXPORT
FaviconProviderHelper *ritual_ZN21FaviconProviderHelperC1Ev() {
  return new FaviconProviderHelper();
}

//  void
//      FaviconProviderHelper::startFaviconRequest(QPointer<FaviconImageRespo
//      nse> faviconResponse)
extern "C" Q_DECL_EXPORT
void ritual_ZN21FaviconProviderHelper19startFaviconRequestE8QPointerI20FaviconImageResponseE(
    FaviconProviderHelper *self,
    const QPointer<FaviconImageResponse> *faviconResponse) {
  self->startFaviconRequest(*faviconResponse);
}

//  QPointer<QQuickWebEngineView>
//      FaviconProviderHelper::findViewByImageSource(const QUrl &imageSource,
//      bool isIconUrl) const
extern "C" Q_DECL_EXPORT
QPointer<QQuickWebEngineView> *ritual_ZNK21FaviconProviderHelper21findViewByImageSourceERK4QUrlb(
    const FaviconProviderHelper *self,
    const QUrl *imageSource,
    bool isIconUrl) {
  return new QPointer<QQuickWebEngineView>(
      self->findViewByImageSource(
          *imageSource,
          isIconUrl));
}

//  a QPointer<QQuickWebEngineView> a ritual of FaviconProviderHelper gave
extern "C" Q_DECL_EXPORT
void ritual_drop_FaviconProviderHelper__QPointer_QQuickWebEngineView(
    QPointer<QQuickWebEngineView> *self) {
  delete self;
}
